# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='HC_decay_sorp_henry_1Du_root',
    task_id='HC_decay_sorp_henry_1Du',
    output_dir='out',
)
model.msh.read_file('HC_decay_sorp_henry_1Du.msh')
model.gli.read_file('HC_decay_sorp_henry_1Du.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='LIQUID_FLOW',
    NUM_TYPE='NEW',
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='MASS_TRANSPORT',
    NUM_TYPE='NEW',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT1'],
    DIS_TYPE=['CONSTANT:', 20000.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='SorbDecay',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT:', 1.0],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='MASS_TRANSPORT',
    PRIMARY_VARIABLE='SorbDecay',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 0.0],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='LIQUID_FLOW',
    PRIMARY_VARIABLE='PRESSURE1',
    GEO_TYPE=['POINT', 'POINT0'],
    DIS_TYPE=['CONSTANT_NEUMANN', 1.157407e-06],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=1,
    GEOMETRY_AREA=1.0,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    STORAGE=[1, 0.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1e-12],
    MASS_DISPERSION=[1, 5.0, 0.0],
    DENSITY=[1, 2000.0],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2000.0],
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    PCS_TYPE='PRESSURE1',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
    HEAT_CAPACITY=[1, 0.0],
    HEAT_CONDUCTIVITY=[1, 0.0],
)
model.mcp.add_block(
    main_key='COMPONENT_PROPERTIES',
    NAME='SorbDecay',
    MOBILE=1,
    DECAY=[1, 2e-07, 1.0],
    ISOTHERM=[1, 6.8e-05],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='LIQUID_FLOW',
    ELE_GAUSS_POINTS=3,
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 1.0, 1, 2],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='MASS_TRANSPORT',
    LINEAR_SOLVER=[2, 6, 1e-14, 1000, 0.5, 1, 2],
    ELE_GAUSS_POINTS=3,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='LIQUID_FLOW',
    TIME_STEPS=[100, 86400.0],
    TIME_END=8640000.0,
    TIME_START=0.0,
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='MASS_TRANSPORT',
    TIME_STEPS=[100, 86400.0],
    TIME_END=8640000.0,
    TIME_START=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['PRESSURE1'],
        ['SorbDecay'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [86400],
        [2160000],
        [4320000],
        [6480000],
        [8640000],
    ],
)
model.write_input()
model.run_model()
