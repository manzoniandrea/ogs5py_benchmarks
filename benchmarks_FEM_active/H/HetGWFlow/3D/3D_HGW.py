# -*- coding: utf-8 -*-
from ogs5py import OGS

model = OGS(
    task_root='3D_HGW_root',
    task_id='3D_HGW',
    output_dir='out',
)
model.msh.read_file('3D_HGW.msh')
model.gli.read_file('3D_HGW.gli')
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='GROUNDWATER_FLOW',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'L_SF'],
    DIS_TYPE=['CONSTANT', 10],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'R_SF'],
    DIS_TYPE=['CONSTANT', 9],
)
model.ic.add_block(
    main_key='INITIAL_CONDITION',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE='DOMAIN',
    DIS_TYPE=['CONSTANT', 10],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='GROUNDWATER_FLOW',
    PRIMARY_VARIABLE='HEAD',
    GEO_TYPE=['SURFACE', 'L_SF'],
    DIS_TYPE=['CONSTANT', 0],
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=3,
    GEOMETRY_AREA=10.0,
    POROSITY=[1, 0.2],
    TORTUOSITY=[1, 1.0],
    PERMEABILITY_TENSOR=['ISOTROPIC', 1.0],
    PERMEABILITY_DISTRIBUTION='K_field_sorted',
)
model.mfp.add_block(
    main_key='FLUID_PROPERTIES',
    FLUID_TYPE='LIQUID',
    DAT_TYPE='LIQUID',
    DENSITY=[1, 1000.0],
    VISCOSITY=[1, 0.001],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='GROUNDWATER_FLOW',
    LINEAR_SOLVER=[2, 5, 1e-12, 2000, 1.0, 100, 4],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='GROUNDWATER_FLOW',
    TIME_START=0.0,
    TIME_END=10000.0,
    TIME_STEPS=[1, 2000.0],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES='HEAD',
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEPS', 1],
)
model.mpd.add(
    name='K_field_sorted',
    file_ext='',
)
model.mpd.read_file('K_field_sorted')
model.write_input()
model.run_model()
