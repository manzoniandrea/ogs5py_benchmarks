# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='m_sphere_elastic_root',
    task_id='m_sphere_elastic',
    output_dir='out',
)
model.msh.read_file('m_sphere_elastic.msh')
model.gli.read_file('m_sphere_elastic.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'oben'],
    DIS_TYPE=['CONSTANT', 0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'unten'],
    DIS_TYPE=['CONSTANT', 0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_N',
    GEO_TYPE=['POLYLINE', 'innen'],
    DIS_TYPE=['CONSTANT_NEUMANN', -1000.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_N',
    GEO_TYPE=['POLYLINE', 'aussen'],
    DIS_TYPE=['CONSTANT_NEUMANN', -101325.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1,
    POROSITY=[1, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 0.0],
    ELASTICITY=[
        ['POISSION', 0.35],
        ['YOUNGS_MODULUS:'],
        [1, 125000000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-15, 5000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 1.0],
    TIME_END=1,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_1'],
        ['STRESS_2'],
        ['STRESS_3'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['NORM_STRESS_1_X'],
        ['NORM_STRESS_1_Y'],
        ['NORM_STRESS_1_Z'],
        ['NORM_STRESS_2_X'],
        ['NORM_STRESS_2_Y'],
        ['NORM_STRESS_2_Z'],
        ['NORM_STRESS_3_X'],
        ['NORM_STRESS_3_Y'],
        ['NORM_STRESS_3_Z'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='PVD',
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_1'],
        ['STRESS_2'],
        ['STRESS_3'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['NORM_STRESS_1_X'],
        ['NORM_STRESS_1_Y'],
        ['NORM_STRESS_1_Z'],
        ['NORM_STRESS_2_X'],
        ['NORM_STRESS_2_Y'],
        ['NORM_STRESS_2_Z'],
        ['NORM_STRESS_3_X'],
        ['NORM_STRESS_3_Y'],
        ['NORM_STRESS_3_Z'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
    ],
    GEO_TYPE=['POLYLINE', 'unten'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
