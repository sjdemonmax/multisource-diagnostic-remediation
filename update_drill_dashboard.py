"""
update_drill_dashboard.py - Adds complete 5-question interactive sets for all 7 prerequisite concepts
with a seamless Question Stepper (Q1 - Q5) and immediate pedagogical verification.
"""

# Let's define the comprehensive 5-question bank for all 7 concepts:
concept_drill_5q = {
    "CONC-FBD-01": [
        {
            "q": "Q1 (Force Reciprocity): Two blocks A (mass 4kg) and B (mass 2kg) are pushed along frictionless ground by an 18N horizontal force. What is the normal contact force between A and B?",
            "opts": ["6 N", "12 N", "18 N", "0 N"],
            "ans": "6 N",
            "expl": "Total mass = 6 kg, acceleration a = 18/6 = 3 m/s^2. For block B alone, the only horizontal force is contact force F_contact = m_B * a = 2 kg * 3 m/s^2 = 6 N."
        },
        {
            "q": "Q2 (Elevator Apparent Weight): An 800 kg elevator cab accelerates downwards at 2.0 m/s^2 (g = 9.8 m/s^2). What is the tension in the hoisting cable?",
            "opts": ["6,240 N", "7,840 N", "9,440 N", "1,600 N"],
            "ans": "6,240 N",
            "expl": "Equation of motion: m*g - T = m*a => T = m*(g - a) = 800 * (9.8 - 2.0) = 800 * 7.8 = 6,240 N."
        },
        {
            "q": "Q3 (Third Law Criterion): Why do the downward gravitational force on a book and the upward normal reaction from a table NOT form a Newton Third Law pair?",
            "opts": ["They act on the same body", "They are unequal in non-equilibrium", "They act in opposite directions", "Normal force is contact while gravity is non-contact"],
            "ans": "They act on the same body",
            "expl": "Third Law action-reaction pairs must act on two mutually interacting distinct bodies. Both forces act on the book, satisfying first-law translational equilibrium."
        },
        {
            "q": "Q4 (Frictional Balance): A block slides down a 30° ramp at constant velocity. What is the coefficient of kinetic friction mu_k?",
            "opts": ["0.577 (tan 30°)", "0.500 (sin 30°)", "0.866 (cos 30°)", "1.000"],
            "ans": "0.577 (tan 30°)",
            "expl": "At constant velocity, net acceleration is zero. m*g*sin(theta) = mu_k * m*g*cos(theta) => mu_k = tan(theta) = tan(30°) = 0.577."
        },
        {
            "q": "Q5 (Pulley Constraint): In an Atwood machine with masses m1 = 3kg and m2 = 5kg over a frictionless pulley, what is the acceleration of the system? (g = 10 m/s^2)",
            "opts": ["2.5 m/s^2", "5.0 m/s^2", "1.25 m/s^2", "10.0 m/s^2"],
            "ans": "2.5 m/s^2",
            "expl": "System acceleration a = (m2 - m1)/(m1 + m2) * g = (5 - 3)/(5 + 3) * 10 = 2/8 * 10 = 2.5 m/s^2."
        }
    ],
    "CONC-VEC-01": [
        {
            "q": "Q1 (Orthogonal Decomposition): A mass m rests on a ramp inclined at angle theta. What is the gravitational component perpendicular to the ramp?",
            "opts": ["m * g * cos(theta)", "m * g * sin(theta)", "m * g * tan(theta)", "m * g"],
            "ans": "m * g * cos(theta)",
            "expl": "The perpendicular component balancing the normal reaction is m*g*cos(theta); m*g*sin(theta) acts parallel down the ramp."
        },
        {
            "q": "Q2 (Vector Addition): Two forces F1 = 30N along the positive x-axis and F2 = 40N along the positive y-axis act on a particle. What is the magnitude of the resultant force?",
            "opts": ["50 N", "70 N", "10 N", "35 N"],
            "ans": "50 N",
            "expl": "R = sqrt(F1^2 + F2^2) = sqrt(30^2 + 40^2) = sqrt(900 + 1600) = sqrt(2500) = 50 N."
        },
        {
            "q": "Q3 (Dot Product Angle): If the dot product of two non-zero vectors A and B is zero (A . B = 0), what is the angle between them?",
            "opts": ["90 degrees (Perpendicular)", "0 degrees (Parallel)", "180 degrees (Antiparallel)", "45 degrees"],
            "ans": "90 degrees (Perpendicular)",
            "expl": "A . B = |A||B|*cos(theta) = 0. Since magnitudes are non-zero, cos(theta) = 0 => theta = 90 degrees."
        },
        {
            "q": "Q4 (Unit Vector Normalization): Find the unit vector in the direction of vector V = 3i + 4j.",
            "opts": ["0.6i + 0.8j", "3i + 4j", "0.5i + 0.5j", "0.7i + 0.7j"],
            "ans": "0.6i + 0.8j",
            "expl": "|V| = sqrt(3^2 + 4^2) = 5. Unit vector u = (3i + 4j)/5 = 0.6i + 0.8j."
        },
        {
            "q": "Q5 (Relative Velocity): Car A moves north at 40 km/h and Car B moves east at 30 km/h. What is the speed of Car B relative to Car A?",
            "opts": ["50 km/h", "70 km/h", "10 km/h", "35 km/h"],
            "ans": "50 km/h",
            "expl": "V_B/A = V_B - V_A = 30i - 40j. Magnitude = sqrt(30^2 + (-40)^2) = 50 km/h."
        }
    ],
    "CONC-NEWTON-02": [
        {
            "q": "Q1 (Constant Acceleration Tension): A 5kg mass is hoisted vertically with constant upward acceleration a = 2 m/s^2. Find the rope tension (g = 10 m/s^2).",
            "opts": ["60 N", "50 N", "40 N", "10 N"],
            "ans": "60 N",
            "expl": "T - m*g = m*a => T = m*(g + a) = 5 * (10 + 2) = 60 N."
        },
        {
            "q": "Q2 (Impulse-Momentum): A 0.2 kg ball moving at 15 m/s strikes a wall and rebounds elastically at 15 m/s. What is the magnitude of impulse delivered by the wall?",
            "opts": ["6.0 N*s", "3.0 N*s", "0.0 N*s", "1.5 N*s"],
            "ans": "6.0 N*s",
            "expl": "Impulse = Delta p = m*(v_f - v_i) = 0.2 * (15 - (-15)) = 0.2 * 30 = 6.0 N*s."
        },
        {
            "q": "Q3 (Variable Force Acceleration): A net force F(t) = 6t acts on a 2kg body starting from rest. What is its velocity at t = 3s?",
            "opts": ["13.5 m/s", "9.0 m/s", "18.0 m/s", "27.0 m/s"],
            "ans": "13.5 m/s",
            "expl": "a(t) = F(t)/m = 3t. v(t) = integral(3t dt) = 1.5 * t^2. At t = 3s, v = 1.5 * 9 = 13.5 m/s."
        },
        {
            "q": "Q4 (Rocket Thrust): A rocket expels gas at a constant relative speed u = 1000 m/s with a mass burn rate dm/dt = 50 kg/s. What is the thrust force on the rocket?",
            "opts": ["50,000 N", "5,000 N", "20 N", "500,000 N"],
            "ans": "50,000 N",
            "expl": "Thrust F = u * (dm/dt) = 1000 m/s * 50 kg/s = 50,000 N."
        },
        {
            "q": "Q5 (Connected Body Tension): Blocks m1 = 4kg and m2 = 6kg connected by a string are pulled horizontally on smooth ice by force F = 30N applied to m2. What is the tension in the string?",
            "opts": ["12 N", "18 N", "30 N", "15 N"],
            "ans": "12 N",
            "expl": "Total acceleration a = 30/(4 + 6) = 3 m/s^2. For m1 alone, string tension provides all acceleration: T = m1 * a = 4 * 3 = 12 N."
        }
    ],
    "CONC-CARB-01": [
        {
            "q": "Q1 (Hyperconjugative Ranking): Which carbocation is thermodynamically most stable?",
            "opts": ["(CH3)3C+ (tert-butyl)", "(CH3)2CH+ (isopropyl)", "CH3CH2+ (ethyl)", "CH3+ (methyl)"],
            "ans": "(CH3)3C+ (tert-butyl)",
            "expl": "Tert-butyl has 9 alpha-C-H bonds providing extensive hyperconjugative overlap with the empty p-orbital, maximizing charge dispersal."
        },
        {
            "q": "Q2 (Carbocation Rearrangement): What is the major intermediate formed when 1-bromopropane ionizes in polar protic solvent?",
            "opts": ["Hydride-shifted 2-propyl carbocation", "Unrearranged primary 1-propyl carbocation", "Methyl-shifted neopentyl carbocation", "Planar allylic radical"],
            "ans": "Hydride-shifted 2-propyl carbocation",
            "expl": "A 1,2-hydride shift converts the transient primary carbocation into a more stable secondary carbocation."
        },
        {
            "q": "Q3 (Resonance vs Induction): Why is the benzyl carbocation (C6H5-CH2+) more stable than typical primary alkyl carbocations?",
            "opts": ["Extensive delocalization across the aromatic pi system", "High sp3 s-character", "Strong -I inductive effect of phenyl group", "Steric inhibition of resonance"],
            "ans": "Extensive delocalization across the aromatic pi system",
            "expl": "The empty p-orbital of the benzylic carbon conjugates directly with the 6 pi-electrons of the benzene ring, generating 4 resonance contributors."
        },
        {
            "q": "Q4 (Allylic vs Vinylic): Why does vinyl chloride (CH2=CH-Cl) fail to undergo ionization to a vinyl carbocation under SN1 conditions?",
            "opts": ["High sp2 electronegativity destabilizes the vacant orbital", "Steric hindrance of the double bond", "Formation of an aromatic transition state", "Hyperconjugative deactivation"],
            "ans": "High sp2 electronegativity destabilizes the vacant orbital",
            "expl": "A vinyl cation holds positive charge in an sp2 hybrid orbital with 33% s-character, making it exceptionally high in energy and resistant to ionization."
        },
        {
            "q": "Q5 (Ring Expansion): When a cyclopentylmethyl carbocation forms, what spontaneous rearrangement occurs?",
            "opts": ["1,2-Bond shift to form a 6-membered cyclohexyl carbocation", "Hydride shift without ring alteration", "Loss of proton to form an allene", "Methyl extrusion"],
            "ans": "1,2-Bond shift to form a 6-membered cyclohexyl carbocation",
            "expl": "Ring expansion from a 5- to a 6-membered ring relieves ring angle strain (109.5° vs 108°) and generates a stable secondary/tertiary cyclohexyl cation."
        }
    ],
    "CONC-HYB-01": [
        {
            "q": "Q1 (Carbocation Geometry): What is the hybridization and bond angle of the positively charged carbon in an alkyl carbocation?",
            "opts": ["sp2, 120° (Trigonal Planar)", "sp3, 109.5° (Tetrahedral)", "sp, 180° (Linear)", "dsp2, 90° (Square Planar)"],
            "ans": "sp2, 120° (Trigonal Planar)",
            "expl": "The carbon has three sigma bonds and zero lone pairs (steric number = 3), adopting sp2 trigonal planar geometry with a perpendicular unhybridized p-orbital."
        },
        {
            "q": "Q2 (s-Character Electronegativity): In which hybrid orbital is electron density held closest to the nucleus?",
            "opts": ["sp (50% s-character)", "sp2 (33% s-character)", "sp3 (25% s-character)", "sp3d (20% s-character)"],
            "ans": "sp (50% s-character)",
            "expl": "Higher s-character concentrates electron density closer to the nucleus, making sp-hybridized carbons the most electronegative."
        },
        {
            "q": "Q3 (Bond Length Order): Arrange C-C single, double, and triple bonds in order of decreasing bond length.",
            "opts": ["Single > Double > Triple", "Triple > Double > Single", "Double > Single > Triple", "Single > Triple > Double"],
            "ans": "Single > Double > Triple",
            "expl": "Single bonds (sp3-sp3, ~1.54 Å) > double bonds (sp2-sp2, ~1.34 Å) > triple bonds (sp-sp, ~1.20 Å)."
        },
        {
            "q": "Q4 (Acidity of Hydrocarbons): Why is ethyne (acetylene, HC#CH) significantly more acidic than ethane (CH3-CH3)?",
            "opts": ["sp carbanion has 50% s-character stabilizing conjugate base", "Ethyne has weaker C-H covalent bond energy", "Acetylene is non-polar while ethane is polar", "Ethane exhibits allylic stabilization"],
            "ans": "sp carbanion has 50% s-character stabilizing conjugate base",
            "expl": "The conjugate base acetylide anion holds its lone pair in an sp orbital with 50% s-character, stabilizing the negative charge near the carbon nucleus."
        },
        {
            "q": "Q5 (Allene Geometry): In propadiene (allene, CH2=C=CH2), what is the hybridization of the central carbon?",
            "opts": ["sp (Linear, 180°)", "sp2 (Trigonal Planar, 120°)", "sp3 (Tetrahedral)", "dsp2"],
            "ans": "sp (Linear, 180°)",
            "expl": "The central carbon forms two double bonds (two sigma and two mutually perpendicular pi bonds), giving steric number 2 and sp hybridization."
        }
    ],
    "CONC-CHAIN-01": [
        {
            "q": "Q1 (Composite Stationary Point): Find the critical stationary point of f(x) = (2x - 3)^4.",
            "opts": ["x = 1.5", "x = 3.0", "x = 0.0", "x = 2.0"],
            "ans": "x = 1.5",
            "expl": "f'(x) = 4*(2x - 3)^3 * 2 = 8*(2x - 3)^3. Setting f'(x) = 0 gives 2x - 3 = 0 => x = 1.5."
        },
        {
            "q": "Q2 (Trig Chain Rule): Evaluate d/dx [ sin(3x^2 + 5) ].",
            "opts": ["6x * cos(3x^2 + 5)", "cos(3x^2 + 5)", "6x * sin(3x^2 + 5)", "-6x * cos(3x^2 + 5)"],
            "ans": "6x * cos(3x^2 + 5)",
            "expl": "Outer derivative d(sin(u)) = cos(u). Inner derivative d(3x^2 + 5)/dx = 6x. Product = 6x * cos(3x^2 + 5)."
        },
        {
            "q": "Q3 (Exponential Composition): Differentiate f(x) = e^(sqrt(x)).",
            "opts": ["(1 / (2*sqrt(x))) * e^(sqrt(x))", "e^(sqrt(x))", "2*sqrt(x) * e^(sqrt(x))", "sqrt(x) * e^(sqrt(x) - 1)"],
            "ans": "(1 / (2*sqrt(x))) * e^(sqrt(x))",
            "expl": "Outer derivative = e^(sqrt(x)). Inner derivative d(sqrt(x))/dx = 1/(2*sqrt(x)). Product = (1/(2*sqrt(x))) * e^(sqrt(x))."
        },
        {
            "q": "Q4 (Logarithmic Base Derivative): Find the derivative of y = ln(cos(x)).",
            "opts": ["-tan(x)", "tan(x)", "sec(x)", "1 / cos(x)"],
            "ans": "-tan(x)",
            "expl": "dy/dx = (1 / cos(x)) * (-sin(x)) = -sin(x)/cos(x) = -tan(x)."
        },
        {
            "q": "Q5 (Second Derivative Chain): If f(x) = (3x + 1)^3, evaluate the second derivative f''(x) at x = 1.",
            "opts": ["216", "54", "72", "162"],
            "ans": "216",
            "expl": "f'(x) = 3*(3x + 1)^2 * 3 = 9*(3x + 1)^2. f''(x) = 9 * 2*(3x + 1) * 3 = 54*(3x + 1). At x = 1: 54*(4) = 216."
        }
    ],
    "CONC-FUNC-01": [
        {
            "q": "Q1 (Composition Evaluation): If f(x) = x^2 + 1 and g(x) = 2x - 3, evaluate f(g(2)).",
            "opts": ["2", "5", "1", "7"],
            "ans": "2",
            "expl": "Evaluate inner: g(2) = 2(2) - 3 = 1. Evaluate outer: f(1) = 1^2 + 1 = 2."
        },
        {
            "q": "Q2 (Domain Restriction): What is the real domain of f(x) = sqrt(4 - x^2)?",
            "opts": ["[-2, 2]", "(-infinity, -2] U [2, infinity)", "[0, 2]", "(-2, 2)"],
            "ans": "[-2, 2]",
            "expl": "Radicand must be non-negative: 4 - x^2 >= 0 => x^2 <= 4 => -2 <= x <= 2, i.e., interval [-2, 2]."
        },
        {
            "q": "Q3 (Inverse Mapping): If f(x) = (3x + 5) / 2, find the inverse function f^(-1)(x).",
            "opts": ["(2x - 5) / 3", "(2x + 5) / 3", "(3x - 5) / 2", "2 / (3x + 5)"],
            "ans": "(2x - 5) / 3",
            "expl": "Set y = (3x + 5)/2 => 2y = 3x + 5 => 3x = 2y - 5 => x = (2y - 5)/3. Therefore f^(-1)(x) = (2x - 5)/3."
        },
        {
            "q": "Q4 (Odd and Even Parity): Which of the following functions satisfies the odd function condition f(-x) = -f(x)?",
            "opts": ["f(x) = x^3 - 4x", "f(x) = x^2 + 3", "f(x) = cos(x)", "f(x) = e^x"],
            "ans": "f(x) = x^3 - 4x",
            "expl": "f(-x) = (-x)^3 - 4(-x) = -x^3 + 4x = -(x^3 - 4x) = -f(x). Polynomial contains only odd powers."
        },
        {
            "q": "Q5 (Range Determination): Find the range of f(x) = 1 / (x^2 + 2) for all real x.",
            "opts": ["(0, 0.5]", "[0, 0.5]", "(0, 1]", "[-0.5, 0.5]"],
            "ans": "(0, 0.5]",
            "expl": "Since x^2 >= 0, the denominator x^2 + 2 in [2, infinity). Hence 1/(x^2 + 2) achieves its maximum 1/2 at x=0 and approaches 0 as x -> infinity."
        }
    ]
}

print(f"Generated comprehensive question bank: {len(concept_drill_5q)} concepts with 5 questions each = {sum(len(v) for v in concept_drill_5q.values())} total questions.")
