# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='m2_3Dloadbt_root',
    task_id='m2_3Dloadbt',
    output_dir='out',
)
model.msh.read_file('m2_3Dloadbt.msh')
model.gli.read_file('m2_3Dloadbt.gli')
model.ddc.read_file('m2_3Dloadbt.ddc')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='NEW',
)
model.rfd.read_file('m2_3Dloadbt.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE1'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [0, 0.0],
        [1, 0.0],
        [2, 0.0],
        [3, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE2'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [4, 0.0],
        [5, 0.0],
        [6, 0.0],
        [7, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE3'],
    DIS_TYPE=[
        ['LINEAR', 4],
        [8, 0.0],
        [9, 0.0],
        [10, 0.0],
        [11, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE4'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [12, 40.0],
        [13, 40.0],
        [14, 40.0],
        [15, 40.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE5'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [16, 0.0],
        [17, 0.0],
        [18, 0.0],
        [19, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE6'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [20, 0.0],
        [21, 0.0],
        [22, 0.0],
        [23, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE7'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [24, -40.0],
        [25, -40.0],
        [26, -40.0],
        [27, -40.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE8'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [28, 0.0],
        [29, 0.0],
        [30, 0.0],
        [31, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE9'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [32, 0.0],
        [33, 0.0],
        [34, 0.0],
        [35, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE10'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [36, 0.0],
        [37, 0.0],
        [38, 0.0],
        [39, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE11'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [40, 40.0],
        [41, 40.0],
        [42, 40.0],
        [43, 40.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE12'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [44, 40.0],
        [45, 40.0],
        [46, 40.0],
        [47, 40.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE13'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [48, -40.0],
        [49, -40.0],
        [50, -40.0],
        [51, -40.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE14'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [52, 0.0],
        [53, 0.0],
        [54, 0.0],
        [55, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE15'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [56, 0.0],
        [57, 0.0],
        [58, 0.0],
        [59, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['SURFACE', 'SURFACE16'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [60, 40.0],
        [61, 40.0],
        [62, 40.0],
        [63, 40.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['SURFACE', 'SURFACE17'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [64, 0.0],
        [65, 0.0],
        [66, 0.0],
        [67, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Z1',
    GEO_TYPE=['SURFACE', 'SURFACE18'],
    DIS_TYPE=[
        ['LINEAR_NEUMANN', 4],
        [68, 0.0],
        [69, 0.0],
        [70, 0.0],
        [71, 0.0],
    ],
    TIM_TYPE=['CURVE', 1],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.25],
        ['YOUNGS_MODULUS'],
        [1, 25000],
    ],
    STRESS_UNIT='MegaPascal',
    CREEP=[0.18, 5.0, 54000.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 1, 1e-10, 10000, 1.0, 101, 4],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_UNIT='DAY',
    TIME_STEPS=[505, 0.002],
    TIME_END=1.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['DISPLACEMENT_Z1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRESS_XZ'],
        ['STRESS_YZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_ZZ'],
        ['STRAIN_XZ'],
        ['STRAIN_YZ'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0.5],
        [1.0],
    ],
)
model.write_input()
model.run_model()
