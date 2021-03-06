"""
Re-generate examples (based on templates), specification documents (based on
owl files) and term README (based on owl files)
@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2015
"""
import os
import sys

REL_PATH = os.path.dirname(os.path.abspath(__file__))
NIDM_PATH = os.path.join(REL_PATH, os.pardir, "nidm")

for component in ["nidm-results", "nidm-experiment"]:
    COMPONENT_SCRIPTS = os.path.join(NIDM_PATH, component, "scripts")
    sys.path.append(COMPONENT_SCRIPTS)

import recompute_all_ex
import UpdateExampleReadmes
import UpdateTermReadme
import create_results_specification
import create_expe_specification


def main():
    # Re-create turtle examples from template
    recompute_all_ex.main()
    # Convert turtle to provn and upload to Prov Store
    UpdateExampleReadmes.main()
    # Update terms README
    UpdateTermReadme.main()
    # Update specifications
    create_results_specification.main("dev")
    create_expe_specification.main()

if __name__ == '__main__':
    main()
