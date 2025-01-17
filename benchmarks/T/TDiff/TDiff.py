# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='TDiff_root',
    task_id='TDiff',
    output_dir='out',
)
model.msh.read_file('TDiff.msh')
model.gli.read_file('TDiff.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='HEAT_TRANSPORT',
    TEMPERATURE_UNIT='KELVIN',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='HEAT_TRANSPORT',
    PRIMARY_VARIABLE='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT', 1],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.1],
    STORAGE=[1, 0.0],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-15],
    HEAT_DISPERSION=[1, 0.0, 0.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2500],
    THERMAL=[
        ['EXPANSION:'],
        [1e-05],
        ['CAPACITY:'],
        [1, 1000],
        ['CONDUCTIVITY:'],
        [1, 3.2],
    ],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.0],
    SPECIFIC_HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='HEAT_TRANSPORT',
    LINEAR_SOLVER=[2, 0, 1e-12, 1000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=2,
    NON_LINEAR_SOLVER=['PICARD', 0.001, 25, 0.0],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='HEAT_TRANSPORT',
    TIME_STEPS=[1000, 390625.0],
    TIME_END=1e+99,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='HEAT_TRANSPORT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POLYLINE', 'ROCK'],
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='HEAT_TRANSPORT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT2'],
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='HEAT_TRANSPORT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT3'],
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='HEAT_TRANSPORT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT4'],
    TIM_TYPE=['STEPS', 1],
)
model.out.add_block(
    main_key='OUTPUT',
    PCS_TYPE='HEAT_TRANSPORT',
    NOD_VALUES='TEMPERATURE1',
    GEO_TYPE=['POINT', 'POINT5'],
    TIM_TYPE=['STEPS', 1],
)
model.write_input()
model.run_model()
