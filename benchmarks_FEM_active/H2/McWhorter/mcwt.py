# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='mcwt_root',
    task_id='mcwt',
    output_dir='out',
)
model.msh.read_file('mcwt.msh')
model.gli.read_file('mcwt.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    NUM_TYPE='NEW',
    ELEMENT_MATRIX_OUTPUT=0,
)
model.rfd.read_file('mcwt.rfd')
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POLYLINE', 'left'],
    DIS_TYPE=['CONSTANT', 5000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE2',
    GEO_TYPE=['POLYLINE', 'left'],
    DIS_TYPE=['CONSTANT', 200000.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MULTI_PHASE_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 50000.0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    POROSITY=[1, 0.3],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-10],
    PERMEABILITY_SATURATION=[
        [6, 0.0, 1.0, 2],
        [66, 0.0, 1.0, 2, 1e-09],
    ],
    CAPILLARY_PRESSURE=[6, 5000],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='GAS',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MULTI_PHASE_FLOW',
    ELE_MASS_LUMPING=1,
    ELE_UPWINDING=[0, 1.0],
    LINEAR_SOLVER=[2, 1, 1e-12, 2000, 1.0, 100, 4],
    NON_LINEAR_SOLVER=['PICARD', 1e-05, 250, 1.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MULTI_PHASE_FLOW',
    TIME_CONTROL=[
        ['PI_AUTO_STEP_SIZE'],
        [1, 0.0001, 1e-10, '10s'],
    ],
    TIME_END=10000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POLYLINE', 'TOP'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [500],
        [1000],
        [2000],
        [4000],
        [7000],
        [10000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [500],
        [1000],
        [2000],
        [4000],
        [7000],
        [10000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['PRESSURE2'],
        ['PRESSURE_W'],
        ['SATURATION1'],
        ['VELOCITY_X1'],
        ['VELOCITY_Y1'],
        ['VELOCITY_X2'],
        ['VELOCITY_Y2'],
    ],
    GEO_TYPE=['POINT', 'POINT4'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
