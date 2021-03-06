"""
Create SPM example 003 stored in nidm/nidm-results/spm/example003 by using the
class templates available in nidm/nidm-results/terms/templates

@author: Camille Maumet <c.m.j.maumet@warwick.ac.uk>
@copyright: University of Warwick 2013-2014
"""
import os
from create_example_from_templates import ExampleFromTemplate

import sys

RELPATH = os.path.dirname(os.path.abspath(__file__))
NIDMRESULTSPATH = os.path.dirname(RELPATH)
# Append parent script directory to path
sys.path.append(os.path.join(NIDMRESULTSPATH, os.pardir, os.pardir, "scripts"))
from Constants import STATO_OLS_STR, STATO_OLS_LABEL, STATO_TSTATISTIC_STR, \
    STATO_TSTATISTIC_LABEL, NIDM_P_VALUE_UNCORRECTED_QNAME, \
    OBO_STATISTIC_QNAME, OBO_P_VALUE_FWER_QNAME


def main():
    nidm_classes = {
        "DesignMatrix": dict(
            design_matrix_id='niiri:design_matrix_id',
            label="Design Matrix",
            location="file:///path/to/DesignMatrix.csv",
            format="text/csv",
            filename="DesignMatrix.csv",
            design_matrix_png_id="niiri:design_matrix_png_id"),
        "Image-DesignMatrix": dict(
            image_id="niiri:design_matrix_png_id",
            location="file:///path/to/DesignMatrix.png",
            filename="DesignMatrix.png",
            format="image/png"
            ),
        "Data": dict(
            data_id='niiri:data_id',
            label="Data",
            scaling="true",
            target=100
            ),
        "ErrorModel": dict(
            error_model_id="niiri:error_model_id",
            noise_distribution="nidm:NIDM_0000032",
            variance_homo="true",
            variance_spatial="nidm:NIDM_0000073",
            dependence="nidm:NIDM_0000048",
            dependence_spatial="nidm:NIDM_0000073"
            ),
        "ModelParametersEstimation": dict(
            model_pe_id="niiri:model_pe_id",
            label="Model parameters estimation",
            est_method=STATO_OLS_STR,
            est_method_comment=STATO_OLS_LABEL,
            design_matrix_id="niiri:design_matrix_id",
            data_matrix_id="niiri:data_id",
            error_model_id="niiri:error_model_id",
            software_id="niiri:software_id"
            ),
        "ParameterEstimateMap_Location-1": dict(
            beta_map_id="niiri:beta_map_id_1",
            label="Beta Map 1",
            location="file:///path/to/ParameterEstimate_0001.nii.gz",
            filename="ParameterEstimate_0001.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE1": dict(
            derived_from_map_id="niiri:beta_map_id_1_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0001.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:beta_map_id_1"
            ),
        "ParameterEstimateMap_Location-2": dict(
            beta_map_id="niiri:beta_map_id_2",
            label="Beta Map 2",
            location="file:///path/to/ParameterEstimate_0002.nii.gz",
            filename="ParameterEstimate_0002.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE2": dict(
            derived_from_map_id="niiri:beta_map_id_2_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0002.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:beta_map_id_2"
            ),
        "ParameterEstimateMap_Location-3": dict(
            beta_map_id="niiri:beta_map_id_3",
            label="Beta Map 3",
            location="file:///path/to/ParameterEstimate_0003.nii.gz",
            filename="ParameterEstimate_0003.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            param_est_id="niiri:model_pe_id"),
        "DerivedMap-PE3": dict(
            derived_from_map_id="niiri:beta_map_id_3_der",
            derived_map_type="nidm:NIDM_0000061",
            filename="beta_0003.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:beta_map_id_3"
            ),
        "CoordinateSpace-1": dict(
            coordinate_space_id="niiri:coordinate_space_id_1",
            label="Coordinate space 1",
            voxel_to_world_mapping="[[-3, 0, 0, 78],[0, 3, 0, -112],[0, 0, 3, \
-50],[0, 0, 0, 1]]",
            voxel_units="[ \\\"mm\\\", \\\"mm\\\", \\\"mm\\\" ]",
            voxel_size="[ 3, 3, 3 ]",
            coord_system="nidm:NIDM_0000051",
            number_of_dim="3",
            dimensions="[ 53, 63, 46 ]"),
        "ResidualMeanSquaresMap": dict(
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            label="Residual Mean Squares Map",
            location="file:///path/to/ResidualMeanSquares.nii.gz",
            filename="ResidualMeanSquares.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            param_est_id="niiri:model_pe_id"),
        "MaskMap_Analysis": dict(  # The analysis mask
            mask_id="niiri:mask_id_1",
            label="Mask",
            location="file:///path/to/Mask.nii.gz",
            filename="Mask.nii.gz",
            user_defined="false",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            generated_by_act_id="niiri:model_pe_id",
            # fixme: also used by niiri:contrast_estimation_id_2
            used_by_act_id="niiri:contrast_estimation_id"),
        "ContrastWeights": dict(
            contrast_id="niiri:contrast_id",
            label="Contrast: listening > reading",
            value="[1, -1, 0, 0]",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="listening > reading"
            ),
        "ContrastWeights-2": dict(
            contrast_id="niiri:contrast_id_2",
            label="Contrast: motor",
            value="[ 0, 0, 1 ]",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="motor"
            ),
        "ContrastEstimation": dict(
            contrast_estimation_id="niiri:contrast_estimation_id",
            label="Contrast estimation 1",
            software_id="niiri:software_id",
            mask_id="niiri:mask_id_1",
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            design_matrix_id="niiri:design_matrix_id",
            contrast_id="niiri:contrast_id",
            param_est_map="niiri:beta_map_id_1"
            ),
        "ContrastEstUsedParamEst-Con1PE2": dict(
            contrast_estimation_id="niiri:contrast_estimation_id",
            param_est_map="niiri:beta_map_id_2"
            ),
        "ContrastEstimation-2": dict(
            contrast_estimation_id="niiri:contrast_estimation_id_2",
            label="Contrast estimation 2",
            software_id="niiri:software_id",
            mask_id="niiri:mask_id_1",
            residual_mean_squares_map_id="niiri:residual_mean_squares_map_id",
            design_matrix_id="niiri:design_matrix_id",
            contrast_id="niiri:contrast_id_2",
            param_est_map="niiri:beta_map_id_3"
            ),
        "ContrastEstUsedParamEst-Con2PE3": dict(
            contrast_estimation_id="niiri:contrast_estimation_id_2",
            param_est_map="niiri:beta_map_id_3"
            ),
        "ContrastMap": dict(
            contrast_map_id="niiri:contrast_map_id",
            label="Contrast Map: listening > reading",
            location="file:///path/to/Contrast_0001.nii.gz",
            format="image/nifti",
            filename="Contrast_0001.nii.gz",
            contrast_name="listening > reading",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            contrast_est_id="niiri:contrast_estimation_id"),
        "ContrastMap-2": dict(
            contrast_map_id="niiri:contrast_map_id_2",
            label="Contrast Map: motor",
            location="file:///path/to/Contrast_0002.nii.gz",
            format="image/nifti",
            filename="Contrast_0002.nii.gz",
            contrast_name="motor",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            contrast_est_id="niiri:contrast_estimation_id_2"),
        "DerivedMap-ContrastMap-2": dict(
            derived_from_map_id="niiri:contrast_map_id_2_der",
            derived_map_type="nidm:NIDM_0000002",
            filename="con_0002.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:contrast_map_id_2"
            ),
        "ContrastStandardErrorMap": dict(
            contrast_standard_error_map_id="niiri:contrast_standard_error_map_\
id",
            label="Contrast 1 Standard Error Map",
            location="file:///path/to/ContrastStandardError_0001.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError_0001.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            contrast_est_id="niiri:contrast_estimation_id"),
        "ContrastStandardErrorMap-2": dict(
            contrast_standard_error_map_id="niiri:contrast_standard_error_map_\
id_2",
            label="Contrast 2 Standard Error Map",
            location="file:///path/to/ContrastStandardError_0002.nii.gz",
            format="image/nifti",
            filename="ContrastStandardError_0002.nii.gz",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            contrast_est_id="niiri:contrast_estimation_id_2"),
        "StatisticMap_T": dict(
            statistic_map_id="niiri:statistic_map_id",
            label="Statistic Map: listening > reading",
            location="file:///path/to/TStatistic_0001.nii.gz",
            format="image/nifti",
            filename="TStatistic_0001.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="listening > reading",
            error_dof="72.9999999990787",
            effect_dof="1",
            sha="e43b6e01b0463fe7d40782137867a...",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id"),
        "DerivedMap-StatMap": dict(
            derived_from_map_id="niiri:statistic_map_id_der",
            derived_map_type="nidm:NIDM_0000076",
            filename="spmT_0001.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:statistic_map_id"
            ),
        "StatisticMap_T-2": dict(
            statistic_map_id="niiri:statistic_map_id_2",
            label="Statistic Map: motor",
            location="file:///path/to/TStatistic_0002.nii.gz",
            format="image/nifti",
            filename="TStatistic_0002.nii.gz",
            statistic_type=STATO_TSTATISTIC_STR,
            stat_type_comment=STATO_TSTATISTIC_LABEL,
            contrast_name="motor",
            error_dof="72.9999999990787",
            effect_dof="1",
            sha="e43b6e01b0463fe7d40782137867a...",
            coordinate_space_id="niiri:coordinate_space_id_1",
            contrast_est_id="niiri:contrast_estimation_id_2"),
        "DerivedMap-StatMap-2": dict(
            derived_from_map_id="niiri:statistic_map_id_2_der",
            derived_map_type="nidm:NIDM_0000076",
            filename="spmT_0002.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:statistic_map_id_2"
            ),
        "HeightThreshold_equivThresh_equivThresh2": dict(
            height_threshold_id="niiri:height_threshold_id",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            label="Height Threshold: p<7.62276079258051e-07 (unc)",
            value="7.62276079258051e-07",
            equiv_thresh="niiri:height_threshold_id_2",
            equiv_thresh2="niiri:height_threshold_id_3"
            ),
        "HeightThreshold-2": dict(
            height_threshold_id="niiri:height_threshold_id_2",
            thresh_type=OBO_STATISTIC_QNAME,
            label="Height Threshold",
            value="5.23529984739211"
            ),
        "HeightThreshold-3": dict(
            height_threshold_id="niiri:height_threshold_id_3",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            label="Height Threshold",
            value="0.05",
            ),
        "ExtentThresholdStat_equivThresh_equivThresh2_clusterSizeResels": dict(
            extent_threshold_id="niiri:extent_threshold_id",
            label="Extent Threshold: k>=10",
            cluster_size_vox="10",
            cluster_size_resels="3.3",
            equiv_thresh="niiri:height_threshold_id_2",
            equiv_thresh2="niiri:height_threshold_id_3"
            ),
        "ExtentThreshold-2": dict(
            extent_threshold_id="niiri:extent_threshold_id_2",
            label="Extent Threshold",
            thresh_type=OBO_P_VALUE_FWER_QNAME,
            value="1",
            ),
        "ExtentThreshold-3": dict(
            extent_threshold_id="niiri:extent_threshold_id_3",
            label="Extent Threshold",
            thresh_type=NIDM_P_VALUE_UNCORRECTED_QNAME,
            value="1",
            ),
        "DisplayMaskMap": dict(
            display_map_id="niiri:display_map_id",
            label="Display Mask Map",
            user_defined="true",
            location="file:///path/to/DisplayMask.nii.gz",
            filename="DisplayMask.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a..."
            ),
        "PeakDefinitionCriteria_MaxPeaks": dict(
            peak_definition_criteria_id="niiri:peak_definition_criteria_id",
            label="Peak Definition Criteria",
            max_num_peaks="3",
            min_dist_peaks="8.0"
            ),
        "ClusterDefinitionCriteria": dict(
            cluster_definition_criteria_id="niiri:cluster_definition_criteria_\
id",
            label="Cluster Connectivity Criterion: 18",
            connectivity="nidm:NIDM_0000128"
            ),
        "ConjunctionInference": dict(
            conj_inference_id="niiri:inference_id",
            label="Conjunction Inference",
            alternative_hyp="nidm:NIDM_0000060",
            stat_map_id_1="niiri:statistic_map_id",
            stat_map_id_2="niiri:statistic_map_id_2",
            height_thresh_id="niiri:height_threshold_id",
            extent_thresh_id="niiri:extent_threshold_id",
            display_mask_id="niiri:display_map_id",
            peak_def_id="niiri:peak_definition_criteria_id",
            cluster_def_id="niiri:cluster_definition_criteria_id",
            mask_id="niiri:mask_id_1",
            software_id="niiri:software_id"
            ),
        "DerivedMap-Contrast": dict(
            derived_from_map_id="niiri:contrast_map_id_der",
            derived_map_type="nidm:NIDM_0000002",
            filename="con_0001.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:contrast_map_id"
            ),
        "NIDMBundle": dict(
            bundle_id="niiri:spm_results_id",
            label="NIDM-Results",
            object_model="nidm:NIDM_0000027",
            version="1.1.0",
            time="2014-05-19T10:30:00.000+01:00"
            ),
        "SPM_ReselsPerVoxelMap": dict(
            resels_per_voxel_map_id="niiri:resels_per_voxel_map_id",
            label="Resels per Voxel Map",
            location="file:///path/to/ReselsPerVoxel.nii.gz",
            filename="ReselsPerVoxel.nii.gz",
            format="image/nifti",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            model_pe_id="niiri:model_pe_id"
            ),
        "SPM_InferenceUsedRPVMap": dict(
            inference_id="niiri:inference_id",
            resels_per_voxel_map_id="niiri:resels_per_voxel_map_id"
        ),
        "DerivedMap-RPV": dict(
            derived_from_map_id="niiri:resels_per_voxel_map_id_der",
            derived_map_type="nidm:NIDM_0000144",
            filename="RPV.nii",
            format="image/nifti",
            sha="e43b6e01b0463fe7d40782137867a...",
            map_id="niiri:resels_per_voxel_map_id"
            ),
        "SPM_Software": dict(
            software_id="niiri:software_id",
            software_type="nlx:nif-0000-00343",
            label="SPM",
            version="12b.5853"
            ),
        "GrandMeanMap": dict(
            grand_mean_map_id="niiri:grand_mean_map_id",
            label="Grand Mean Map",
            location="file:///path/to/GrandMean.nii.gz",
            filename="GrandMean.nii.gz",
            format="image/nifti",
            masked_median="115",
            coordinate_space_id="niiri:coordinate_space_id_1",
            sha="e43b6e01b0463fe7d40782137867a...",
            model_pe_id="niiri:model_pe_id"
            )
        }

    NIDM_SPM_DIR = os.path.join(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))), 'spm', "example003")
    ttl_file = os.path.join(NIDM_SPM_DIR, 'spm_results_conjunction.ttl')
    example = ExampleFromTemplate(nidm_classes, ttl_file, False)
    example.create_example()

if __name__ == '__main__':
    main()
