# -*- coding: utf-8 -*-
from __future__ import division, print_function
from ogs5py import OGS

model = OGS(
    task_root='m_excav_root',
    task_id='m_excav',
    output_dir='out',
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'RIGHT'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_X1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT', 0.0],
)
model.bc.add_block(
    main_key='BOUNDARY_CONDITION',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='DISPLACEMENT_Y1',
    GEO_TYPE=['POLYLINE', 'BOTTOM'],
    DIS_TYPE=['CONSTANT:', 0.0],
)
model.gli.read_file('m_excav.gli')
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.mmp.add_block(
    main_key='MEDIUM_PROPERTIES',
    GEOMETRY_DIMENSION=2,
    GEOMETRY_AREA=1.0,
)
model.msh.read_file('m_excav.msh')
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 2.85388127854e-05],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 2.85388127854e-05],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.msp.add_block(
    main_key='SOLID_PROPERTIES',
    DENSITY=[1, 2700.0],
    THERMAL=[
        ['EXPANSION', 1e-05],
        ['CAPACITY:'],
        [1, 2.85388127854e-05],
        ['CONDUCTIVITY:'],
        [1, 3.0],
    ],
    ELASTICITY=[
        ['POISSION', 0.3],
        ['YOUNGS_MODULUS:'],
        [1, 35000000000.0],
    ],
)
model.num.add_block(
    main_key='NUMERICS',
    PCS_TYPE='DEFORMATION',
    LINEAR_SOLVER=[2, 0, 1e-12, 5000, 1.0, 100, 4],
    ELE_GAUSS_POINTS=3,
    GRAVITY_PROFILE=1,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE='DOMAIN',
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [0.02],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
    AMPLIFIER=0.0,
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'H_PROFILE'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POLYLINE', 'LEFT'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=[
        [0],
        [1],
        [10],
        [100],
        [1000],
        [10000],
        [100000],
        [1000000],
    ],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT1'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT2'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT15'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT7'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT8'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT9'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT10'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT11'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT12'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.out.add_block(
    main_key='OUTPUT',
    NOD_VALUES=[
        ['DISPLACEMENT_X1'],
        ['DISPLACEMENT_Y1'],
        ['STRESS_XX'],
        ['STRESS_XY'],
        ['STRESS_YY'],
        ['STRESS_ZZ'],
        ['STRAIN_XX'],
        ['STRAIN_XY'],
        ['STRAIN_YY'],
        ['STRAIN_PLS'],
    ],
    GEO_TYPE=['POINT', 'POINT13'],
    DAT_TYPE='TECPLOT',
    TIM_TYPE=['STEP', 4],
)
model.pcs.add_block(
    main_key='PROCESS',
    PCS_TYPE='DEFORMATION',
    NUM_TYPE='EXCAVATION',
)
model.rfd.add_block(
    PROJECT=['BGR', 'D-THM1', 'Test', 'Case.', 'WW'],
)
model.rfd.add_block(
    CURVE=[
        [0, 102.2080114],
        [0.001, 102.2060415],
        [0.002, 102.2040679],
        [0.003, 102.2020909],
        [0.004, 102.2001067],
        [0.005, 102.1981297],
        [0.006, 102.1961562],
        [0.007, 102.1941685],
        [0.008, 102.192195],
        [0.009, 102.1902073],
        [0.01, 102.1882338],
        [0.1, 102.0085724],
        [0.2, 101.8057735],
        [0.3, 101.5997207],
        [0.4, 101.3906016],
        [0.5, 101.1785115],
        [0.6, 100.9636133],
        [0.7, 100.7460483],
        [0.8, 100.5259616],
        [0.9, 100.3034698],
        [1, 100.0787393],
        [2, 97.73837098],
        [3, 95.32695935],
        [4, 92.98449016],
        [5, 90.85098805],
        [6, 89.06647766],
        [7, 87.14702498],
        [8, 85.75219696],
        [9, 84.3879161],
        [10, 83.05347151],
        [20, 71.20639902],
        [30, 61.67893752],
        [40, 53.99014512],
        [50, 47.75994534],
        [60, 42.6879312],
        [70, 38.5366398],
        [80, 35.11829643],
        [90, 32.28438112],
        [100, 29.91739851],
        [200, 18.49336023],
        [300, 14.08804317],
        [400, 11.46656806],
        [500, 9.757062153],
        [600, 8.626562417],
        [700, 7.877451298],
        [800, 7.380922824],
        [900, 6.365382568],
        [1000, 5.933976815],
        [2000, 3.617743457],
        [3000, 2.819106815],
        [4000, 2.430545608],
        [5000, 2.18265627],
        [6000, 2.002828716],
        [7000, 1.866287807],
        [8000, 1.761107521],
        [9000, 1.695093532],
        [10000, 1.514035179],
        [20000, 0.876643851],
        [30000, 0.579402291],
        [40000, 0.397714392],
        [50000, 0.286472066],
        [60000, 0.218360766],
        [70000, 0.176655062],
        [80000, 0.151119514],
        [90000, 0.135486949],
        [100000, 0.125912887],
        [200000, 0.081356539],
        [300000, 0.068518029],
        [400000, 0.060747725],
        [500000, 0.056040271],
        [600000, 0.053189627],
        [700000, 0.051460142],
        [800000, 0.050416792],
        [900000, 0.049783708],
        [1000000, 0.049398199],
        [10000000000.0, 0.049398199],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 5000000.0],
        [10000000000.0, 5000000.0],
    ],
)
model.rfd.add_block(
    CURVE=[
        [0.0, 0.0],
        [10, 10000000.0],
        [10000000000.0, 10000000.0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['NULL', 'NULL'],
        ['EXCAVATION_DOMAIN', 0],
    ],
)
model.st.add_block(
    main_key='SOURCE_TERM',
    PCS_TYPE='DEFORMATION',
    PRIMARY_VARIABLE='EXCAVATION',
    GEO_TYPE=[
        ['POLYLINE', 'ARC2'],
        ['EXCAVATION_DOMAIN', 2],
    ],
)
model.tim.add_block(
    main_key='TIME_STEPPING',
    PCS_TYPE='DEFORMATION',
    TIME_STEPS=[1, 0.02],
    TIME_END=0.02,
    TIME_START=0.0,
)
model.write_input()
model.run_model()