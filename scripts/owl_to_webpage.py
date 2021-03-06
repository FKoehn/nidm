import os
import codecs
from OwlReader import OwlReader
from Constants import *
import re
import cgi

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDM_ROOT = os.path.dirname(RELPATH)
DOC_FOLDER = os.path.join(NIDM_ROOT, 'doc', 'content', 'specs')
INCLUDE_FOLDER = os.path.join(DOC_FOLDER, "include")


class OwlSpecification(object):

    def __init__(self, owl_file, import_files, spec_name, subcomponents=None,
                 used_by=None, generated_by=None, derived_from=None,
                 prefix=None):
        self.owl = OwlReader(owl_file, import_files)
        self.owl.graph.bind('nidm', 'http://purl.org/nidash/nidm#')
        self.name = spec_name
        self.component = self.name.lower().replace("-", "_")
        self.section_open = 0
        self.already_defined_classes = list()

        self.attributes_done = set()
        self.text = ""
        self.create_specification(subcomponents, used_by, generated_by,
                                  derived_from, prefix)

    def create_specification(self, subcomponents, used_by, generated_by,
                             derived_from, prefix):
        self.create_title(self.name+": Types and relations")

        # If no subcomponents are defined display all classes
        if not subcomponents:
            subcomponents = dict([(None, self.owl.classes)])

        table_num = 3
        for subcomponent_name, classes in subcomponents.items():
            classes_by_types = self.owl.get_class_names_by_prov_type(
                classes,
                prefix=prefix, but=self.already_defined_classes)
            self.already_defined_classes += classes

            self.create_subcomponent_table(classes_by_types, table_num,
                                           subcomponent_name)
            table_num = table_num + 1
            all_classes = sorted(classes_by_types[PROV['Agent']]) + \
                sorted(classes_by_types[PROV['Activity']]) + \
                sorted(classes_by_types[PROV['Entity']]) + \
                sorted(classes_by_types[None])

            for class_name in all_classes:
                self.create_class_section(
                    class_name,
                    self.owl.get_definition(class_name),
                    self.owl.attributes.setdefault(class_name, None),
                    used_by, generated_by, derived_from)

            if subcomponent_name:
                self.text += """
            </section>"""

        self.close_sections()

    def create_subcomponent_table(self, classes, table_num,
                                  subcomponent_name=None):
        if subcomponent_name:
            self.text += """
        <section><h1>"""+subcomponent_name+"""</h1>"""
            # Check if there is a header file to include here
            fname = os.path.join(
                INCLUDE_FOLDER,
                self.component+"_" +
                subcomponent_name.split(" ")[0].lower()+".html")
            if os.path.isfile(fname):
                fid = open(fname, "r")
                self.text += fid.read()
                fid.close()

        else:
            subcomponent_name = ""

        # Did not find how to handle table numbering and ids with Respec as we
        # did for figures?
        table_id = "prov-mapping-"""+subcomponent_name.lower()
        self.text += """
        <div style="text-align: left;">
            <table class="thinborder" \
            style="margin-left: auto; margin-right: auto;">
                <caption id=\""""+table_id+"""\">\
                <a class="internalDFN" href=\"#"""+table_id+"""\">\
                Table """+str(table_num)+"""</a>:
                Mapping of """+self.name+""" """+subcomponent_name + \
            """ Core Concepts to types and relations \
                and PROV core concepts</caption> \
                <tbody>
                    <tr>
                        <td><b>"""+self.name+""" Concepts</b></td>
                        <td><b>Types or Relation (PROV concepts)</b></td>
                        <td><b>Name</b></td>
                    </tr>
        """

        self.text += """
        <!-- HERE ------------- Beginning of PROV Entities ------------- -->
        """

        for prov_class in list([
                PROV['Agent'],
                PROV['Activity'],
                PROV['Entity']]):
            sorted_classes = sorted(classes[prov_class])
            for class_uri in sorted_classes:
                self.text += """
                        <tr>
                            <td>"""+self.term_link(class_uri)+"""
                            </td>
                    """

                # First iteration
                if class_uri is sorted_classes[0]:
                    self.text += """
                                <td rowspan=\""""+str(len(sorted_classes)) + \
                        """\" style="text-align: center;">""" + \
                        self.name+""" Types<br/> \
                                (PROV """ + \
                        self.owl.get_label(prov_class).replace('prov:', '') + \
                        """)</td>
                        """

                self.text += """
                                <td>"""+self.term_link(class_uri)+"""</td>
                            </tr>
                """

        self.text += """
                </tbody>
                </table>
            </div>"""

    def create_title(self, title):
        self.text += """
        <section>
            <h1>"""+title+"""</h1>
        """
        self.section_open += 1

    def _format_markdown(self, text):
        # Replace links specified in markdown by html
        match = re.search(r'\[(?P<name>.*)\]\((?P<link>.*)\)', text)
        if match:
            text = text.replace(
                match.group(),
                '<a href="'+match.group('link')+'">' +
                match.group('name')+'</a>')

        return text

    def format_definition(self, definition):
        # Capitalize first letter of definition
        if definition:
            definition = definition[0].upper() + definition[1:]
            definition = self._format_markdown(definition)

        return definition

    def linked_listing(self, uri_list, prefix="", suffix=""):
        linked_listing = prefix

        for i, uri in enumerate(self.owl.sorted_by_labels(uri_list)):
            if i == 0:
                sep = ""
            elif i == len(uri_list):
                sep = " and "
            else:
                sep = ", "
            linked_listing += sep+self.term_link(uri)

        return linked_listing+suffix

    def term_link(self, term_uri, tag="a", text=None):
        href = ""
        if self.owl.is_external_namespace(term_uri):
            href = " href =\""+str(term_uri)+"\""

        if text is None:
            text = self.owl.get_label(term_uri)

        term_link = "<" + tag + " title=\"" + self.owl.get_name(term_uri) + \
                    "\"" + href + ">" + text+"</"+tag+">"

        # # This could be handled by Respec, here we overwrite the id and href
        # # fields in order to be able to have an id that is not generated from
        # # the title field. e.g. title = nidm_0000001 (nidm:Map) and
        # # id = nidm_0000001
        # name_lw = self.owl.get_name(term_uri).lower()
        # if tag is "dfn":
        #     link_info = " id=\"dfn-" + name_lw + "\""
        # elif tag is "a":
        #     link_info = " href=\"#dfn-" + name_lw + "\""

        # term_link = "<" + tag + link_info + \
        #             "  class=\"internalDFN\"" + \
        #             " title=\"" + self.owl.get_name(term_uri) + \
        #             " (" + self.owl.get_label(term_uri) + ")" + \
        #             "\"" + href + ">" + text + "</" + tag + ">"

        if tag is "dfn":
            # Add link to current definition
            term_link = self.term_link(term_uri, text=term_link)

        return term_link

    def create_class_section(self, class_uri, definition, attributes,
                             used_by=None, generated_by=None,
                             derived_from=None, children=False):
        class_label = self.owl.get_label(class_uri)
        class_name = self.owl.get_name(class_uri)

        definition = self.format_definition(definition)

        self.text += """
            <!-- """+class_label+""" ("""+class_name+""")"""+""" -->
            <section id="section-"""+class_label+"""">
                <h1 label=\""""+class_name+"""\">"""+class_label+"""</h1>
                <div class="glossary-ref">
                    """+self.term_link(class_uri, "dfn") + ": " + definition

        self.text += " "+self.term_link(class_uri)+" is"

        prov_class = self.owl.get_prov_class(class_uri)
        if prov_class:
            self.text += " a "+self.owl.get_label(prov_class)

        found_used_by = False
        if used_by:
            if class_uri in used_by:
                self.text += self.linked_listing(used_by[class_uri],
                                                 " used by ")
                found_used_by = True
            used_entities = list()

            for used_entity, used_activities in used_by.items():
                for used_act in used_activities:
                    if used_act == class_uri:
                        used_entities.append(used_entity)
            if used_entities:
                self.text += self.linked_listing(used_entities,
                                                 " that uses ",
                                                 " entities")

        found_generated_by = False
        if generated_by:
            if class_uri in generated_by:
                if found_used_by:
                    self.text += " and "

                self.text += self.linked_listing(
                    list([generated_by[class_uri]]), " generated by ")

                found_generated_by = True

            if class_uri in generated_by.values():
                generated_entities = list()
                for generated_entity, generated_act in generated_by.items():
                    if generated_act == class_uri:
                        generated_entities.append(generated_entity)

                if generated_entities:
                    self.text += self.linked_listing(
                        generated_entities,
                        ". This activity generates ", " entities")

        if derived_from:
            if class_uri in derived_from:
                if found_used_by or found_generated_by:
                    self.text += " and "

                self.text += self.linked_listing(
                    list([derived_from[class_uri]]), " derived from ")

        self.text += "."

        range_classes = list()

        if attributes and (attributes != set([CRYPTO['sha512']])):
            self.text += """
                </div>
                <p></p>
                <div class="attributes" id="attributes-"""+class_label + \
                """"> A """ + \
                self.term_link(class_uri)+""" has attributes:
                <ul>
                    <li><span class="attribute" id=\"""" + \
                class_label+""".label">rdfs:label</span>: \
                    (<em class="rfc2119" title="OPTIONAL">OPTIONAL</em>) """\
            """Human readable description of the """ + \
                self.term_link(class_uri)+""".</li>"""

            for att in sorted(attributes):

                # Do not display prov relations (used, wasGeneratedBy...) as
                # attributes
                if not self.owl.get_label(att).startswith("prov"):
                    if att not in self.attributes_done:
                        # First definition of this attribute
                        att_tag = "dfn"
                    else:
                        att_tag = "a"

                    self.attributes_done.add(att)

                    # if att_label.startswith("nidm:"):
                    att_def = self.owl.get_definition(att)
                    self.text += """
                        <li>"""+self.term_link(att, att_tag) + \
                        '</span>: (<em class="rfc2119" title="OPTIONAL">' + \
                        'OPTIONAL</em>) ' + self.format_definition(att_def)

                    if att in self.owl.parent_ranges:
                        child_ranges = list()
                        for parent_range in self.owl.parent_ranges[att]:
                            child_ranges += self.owl.get_direct_children(
                                parent_range)
                        child_ranges = sorted(child_ranges)

                        # if nidm_namespace:
                        child_range_txt = ""
                        if child_ranges:
                            # Get all child ranges
                            child_range_txt = self.linked_listing(
                                child_ranges, " such as ")

                        self.text += self.linked_listing(
                            self.owl.parent_ranges[att],
                            " (range ", child_range_txt+")")
                        self.text += "."

                        for range_class in sorted(self.owl.ranges[att]):
                            if self.owl.get_label(range_class).\
                                    startswith('nidm'):
                                range_classes.append(range_class)

                        self.text += "</li>"

        BASE_REPOSITORY = "https://raw.githubusercontent.com/" + \
            "incf-nidash/nidm/master/"
        examples = self.owl.get_example(class_uri, BASE_REPOSITORY)
        for example in sorted(examples):
            self.text += """
                </ul>
                </div>
                <pre class='example highlight'>"""+cgi.escape(example) + \
                """</pre>"""

        for range_name in range_classes:
            if not range_name in self.already_defined_classes:
                self.already_defined_classes.append(range_name)
                self.create_class_section(
                    range_name,
                    self.owl.get_definition(range_name),
                    self.owl.attributes.setdefault(range_name, None),
                    children=True)

        # For object property list also children (in sub-sections)
        if children:
            direct_children = self.owl.sorted_by_labels(
                self.owl.get_direct_children(class_uri))
            for child in direct_children:
                if not child in self.already_defined_classes:
                    self.create_class_section(
                        child,
                        self.owl.get_definition(child),
                        self.owl.attributes.setdefault(child, None),
                        children=True)
                    self.already_defined_classes.append(child)

        # Display individuals
        individuals = self.owl.sorted_by_labels(
            self.owl.get_individuals(class_uri))
        if individuals:
            self.text += \
                " Examples of "+self.term_link(class_uri)+" includes " + \
                "<ul>"

            for indiv in individuals:
                self.text += "<li>" + self.term_link(indiv, "dfn") + ": " + \
                             self.format_definition(
                                 self.owl.get_definition(indiv)) + \
                             "</li>"

            self.text += "</ul>"

        self.text += """
            </section>"""

    def close_sections(self):
        for x in range(0, self.section_open):
            self.text += "\t"*x+"</section>\n"

    # Write out specification
    def write_specification(self, spec_file=None, component=None,
                            version=None):
        if component and version:
            spec_file = os.path.join(DOC_FOLDER, component+"_"+version+".html")

        spec_open = codecs.open(spec_file, 'w', "utf-8")
        spec_open.write(self.text)
        spec_open.close()

    def _header_footer(self, prev_file=None, follow_file=None, component=None,
                       version=None):

        release_notes = None
        if component:
            prev_file = os.path.join(INCLUDE_FOLDER, component+"_head.html")
            follow_file = os.path.join(INCLUDE_FOLDER, component+"_foot.html")
            if version:
                release_notes = os.path.join(
                    os.path.dirname(self.owl.file),
                    component+"_"+version+"_notes.html")
                if not os.path.isfile(release_notes):
                    release_notes = None

        if prev_file is not None:
            prev_file_open = open(prev_file, 'r')
            self.text = prev_file_open.read().decode('utf-8')+self.text
            prev_file_open.close()
        if release_notes is not None:
            release_note_open = open(release_notes, 'r')
            self.text = self.text+release_note_open.read()
            release_note_open.close()
        if follow_file is not None:
            follow_file_open = open(follow_file, 'r')
            self.text = self.text+follow_file_open.read()
            follow_file_open.close()
