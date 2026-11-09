"""
generate_dataset.py - Generates the multi-source diagnostic retrieval corpora:
1. input 1.csv: Concept-tagged question bank (250 questions with prerequisite linkages)
2. input 2.csv: Longitudinal student diagnostic exam logs (150 students across 3 mock tests)
3. artifact 2.csv: Misconception taxonomy & platform remediation resource library
"""

import os
import random
import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

base_dir = os.path.dirname(os.path.abspath(__file__))

# ----------------------------------------------------------------------
# 1. GENERATE input 1.csv: Concept-Tagged Question Bank (250 Questions)
# ----------------------------------------------------------------------
concepts_data = [
    # Physics - Mechanics
    {"concept_id": "CONC-VEC-01", "name": "Vector Resolution & Components", "chapter": "Vectors & Kinematics", "subject": "Physics", "prereq": "CONC-TRIG-01"},
    {"concept_id": "CONC-NEWTON-01", "name": "Newton's First Law (Inertia)", "chapter": "Laws of Motion", "subject": "Physics", "prereq": "CONC-VEC-01"},
    {"concept_id": "CONC-NEWTON-02", "name": "Newton's Second Law (F=ma)", "chapter": "Laws of Motion", "subject": "Physics", "prereq": "CONC-NEWTON-01"},
    {"concept_id": "CONC-FBD-01", "name": "Free Body Diagram Force Analysis", "chapter": "Laws of Motion", "subject": "Physics", "prereq": "CONC-NEWTON-02"},
    {"concept_id": "CONC-NEWTON-03", "name": "Newton's Third Law (Action-Reaction)", "chapter": "Laws of Motion", "subject": "Physics", "prereq": "CONC-FBD-01"},
    {"concept_id": "CONC-FRIC-01", "name": "Static & Kinetic Friction Constraints", "chapter": "Laws of Motion", "subject": "Physics", "prereq": "CONC-FBD-01"},
    {"concept_id": "CONC-MOM-01", "name": "Linear Momentum Conservation", "chapter": "Work, Energy & Momentum", "subject": "Physics", "prereq": "CONC-NEWTON-03"},
    {"concept_id": "CONC-CIRC-01", "name": "Centripetal Acceleration & Dynamics", "chapter": "Circular Motion", "subject": "Physics", "prereq": "CONC-NEWTON-02"},
    {"concept_id": "CONC-ROT-01", "name": "Torque & Angular Equilibrium", "chapter": "Rotational Mechanics", "subject": "Physics", "prereq": "CONC-FBD-01"},
    {"concept_id": "CONC-THERM-01", "name": "Carnot Cycle & Heat Engine Efficiency", "chapter": "Thermodynamics", "subject": "Physics", "prereq": "CONC-NEWTON-02"},
    
    # Chemistry - Organic & Physical
    {"concept_id": "CONC-STR-01", "name": "Lewis Structures & Formal Charge", "chapter": "Chemical Bonding", "subject": "Chemistry", "prereq": "CONC-ATOM-01"},
    {"concept_id": "CONC-HYB-01", "name": "Orbital Hybridization (sp3, sp2, sp)", "chapter": "Chemical Bonding", "subject": "Chemistry", "prereq": "CONC-STR-01"},
    {"concept_id": "CONC-ELEC-01", "name": "Inductive & Resonance Electron Effects", "chapter": "General Organic Chemistry", "subject": "Chemistry", "prereq": "CONC-HYB-01"},
    {"concept_id": "CONC-CARB-01", "name": "Carbocation Stability & Rearrangement", "chapter": "General Organic Chemistry", "subject": "Chemistry", "prereq": "CONC-ELEC-01"},
    {"concept_id": "CONC-SN2-01", "name": "SN2 Bimolecular Nucleophilic Substitution", "chapter": "Haloalkanes", "subject": "Chemistry", "prereq": "CONC-CARB-01"},
    {"concept_id": "CONC-SN1-01", "name": "SN1 Unimolecular Substitution & Racemization", "chapter": "Haloalkanes", "subject": "Chemistry", "prereq": "CONC-CARB-01"},
    {"concept_id": "CONC-KINET-01", "name": "Reaction Orders & Rate Law Kinetics", "chapter": "Chemical Kinetics", "subject": "Chemistry", "prereq": "CONC-STR-01"},
    {"concept_id": "CONC-EQUIL-01", "name": "Le Chatelier's Principle & Dynamic Equilibrium", "chapter": "Chemical Equilibrium", "subject": "Chemistry", "prereq": "CONC-KINET-01"},
    
    # Mathematics - Calculus & Algebra
    {"concept_id": "CONC-FUNC-01", "name": "Domain, Range & Composite Functions", "chapter": "Functions & Relations", "subject": "Mathematics", "prereq": "CONC-ALG-01"},
    {"concept_id": "CONC-LIM-01", "name": "Evaluation of Limits & Indeterminate Forms", "chapter": "Limits & Continuity", "subject": "Mathematics", "prereq": "CONC-FUNC-01"},
    {"concept_id": "CONC-DERIV-01", "name": "Fundamental Derivatives & Power Rule", "chapter": "Differential Calculus", "subject": "Mathematics", "prereq": "CONC-LIM-01"},
    {"concept_id": "CONC-CHAIN-01", "name": "Chain Rule for Composite Differentiation", "chapter": "Differential Calculus", "subject": "Mathematics", "prereq": "CONC-DERIV-01"},
    {"concept_id": "CONC-MAX-01", "name": "Maxima, Minima & Optimization Derivatives", "chapter": "Applications of Derivatives", "subject": "Mathematics", "prereq": "CONC-CHAIN-01"},
    {"concept_id": "CONC-INTEG-01", "name": "Definite Integration by Substitution", "chapter": "Integral Calculus", "subject": "Mathematics", "prereq": "CONC-CHAIN-01"},
    {"concept_id": "CONC-VECALG-01", "name": "Dot & Cross Products in 3D Geometry", "chapter": "Vector & 3D Geometry", "subject": "Mathematics", "prereq": "CONC-FUNC-01"}
]

questions_list = []
qid = 1

# Generate 250 questions mapped to concepts
for i in range(250):
    c = concepts_data[i % len(concepts_data)]
    subj = c["subject"]
    chap = c["chapter"]
    cid = c["concept_id"]
    cname = c["name"]
    prereq = c["prereq"]
    
    if subj == "Physics":
        q_text = f"A mass-block system subject to {cname.lower()} is placed on an inclined plane. Determine the resulting force balance equation."
        opt_a = f"F_net = m * a with proper normal reaction decomposition"
        opt_b = f"Action and reaction cancel internally on the same body"
        opt_c = f"Normal force equals m*g without angle cosine factor"
        opt_d = f"Frictional resistance is independent of normal force"
        correct = "A"
        distractor = "B:Action-Reaction on Same Body Misconception|C:Missing Projection Factor|D:Friction Normal Decoupling"
    elif subj == "Chemistry":
        q_text = f"In an entrance exam reaction mechanism governed by {cname.lower()}, a chiral alkyl halide undergoes substitution. Predict the major product."
        opt_a = f"Complete Walden inversion with 100% optical purity"
        opt_b = f"Planar carbocation formation yielding a 50:50 racemic mixture"
        opt_c = f"Rearranged carbocation leading to an unexpected elimination alkene"
        opt_d = f"No reaction due to high steric hindrance of primary substrate"
        correct = "A" if "SN2" in cname else "B"
        distractor = "B:Intermediate Planar Carbocation Confusion|C:Unwarranted Rearrangement|D:Steric Misclassification"
    else:
        q_text = f"Evaluate the critical boundary condition for the function f(x) utilizing {cname.lower()} over the interval [0, 2pi]."
        opt_a = f"Strict differentiation using inner derivative scaling factor"
        opt_b = f"Direct algebraic cancellation ignoring inner derivative"
        opt_c = f"Limit evaluation yielding undefined discontinuity"
        opt_d = f"Linear approximation without higher order expansion"
        correct = "A"
        distractor = "B:Omission of Inner Chain Derivative|C:False Discontinuity Inference|D:Incomplete Taylor Expansion"
        
    diff = "Standard" if i % 3 == 0 else ("Advanced" if i % 3 == 1 else "Conceptual")
    
    questions_list.append({
        "question_id": f"QSTN-{subj[:3].upper()}-{qid:03d}",
        "subject": subj,
        "chapter": chap,
        "primary_concept_id": cid,
        "primary_concept_name": cname,
        "prerequisite_concept_id": prereq,
        "question_text": q_text,
        "option_a": opt_a,
        "option_b": opt_b,
        "option_c": opt_c,
        "option_d": opt_d,
        "correct_option": correct,
        "distractor_misconceptions": distractor,
        "difficulty_tier": diff
    })
    qid += 1

questions_df = pd.DataFrame(questions_list)
questions_df.to_csv(os.path.join(base_dir, "input 1.csv"), index=False)
print(f"✅ Created input 1.csv: {len(questions_df)} questions across {questions_df['subject'].nunique()} subjects.")

# ----------------------------------------------------------------------
# 2. GENERATE artifact 2.csv: Misconception Taxonomy & Remediation Library
# ----------------------------------------------------------------------
remediation_data = [
    {
        "misconception_id": "MISC-PHYS-01",
        "surface_concept_id": "CONC-NEWTON-03",
        "surface_concept_name": "Newton's Third Law (Action-Reaction)",
        "root_cause_prerequisite_id": "CONC-FBD-01",
        "root_cause_prerequisite_name": "Free Body Diagram Force Analysis",
        "prerequisite_gap_depth": 1,
        "misconception_description": "Believing action-reaction pairs act on the same body and cancel each other out.",
        "remediation_module_id": "MOD-PHYS-FBD-04",
        "lecture_title": "Mastering Free Body Diagrams: Isolated System Force Pairs",
        "video_timestamp_range": "14:20 - 18:45 (4m 25s)",
        "assigned_practice_set_id": "DRILL-FBD-05Q",
        "practice_set_name": "5-Question Micro-Drill: Isolating Action-Reaction Reciprocity",
        "remediation_duration_min": 25,
        "expected_score_lift_pct": 16.5
    },
    {
        "misconception_id": "MISC-PHYS-02",
        "surface_concept_id": "CONC-FBD-01",
        "surface_concept_name": "Free Body Diagram Force Analysis",
        "root_cause_prerequisite_id": "CONC-VEC-01",
        "root_cause_prerequisite_name": "Vector Resolution & Components",
        "prerequisite_gap_depth": 2,
        "misconception_description": "Scalar addition of orthogonal forces without projecting along perpendicular axes.",
        "remediation_module_id": "MOD-PHYS-VEC-02",
        "lecture_title": "Vector Decompositions on Inclined Planes & Pulley Constraints",
        "video_timestamp_range": "08:15 - 12:30 (4m 15s)",
        "assigned_practice_set_id": "DRILL-VEC-05Q",
        "practice_set_name": "5-Question Micro-Drill: Resolving Normal & Gravitational Projections",
        "remediation_duration_min": 20,
        "expected_score_lift_pct": 14.8
    },
    {
        "misconception_id": "MISC-PHYS-03",
        "surface_concept_id": "CONC-ROT-01",
        "surface_concept_name": "Torque & Angular Equilibrium",
        "root_cause_prerequisite_id": "CONC-NEWTON-02",
        "root_cause_prerequisite_name": "Newton's Second Law (F=ma)",
        "prerequisite_gap_depth": 1,
        "misconception_description": "Confusing net force zero with net torque zero in rigid body dynamics.",
        "remediation_module_id": "MOD-PHYS-ROT-05",
        "lecture_title": "Rigid Body Equilibrium: Decoupling Translational and Rotational Acceleration",
        "video_timestamp_range": "22:10 - 27:00 (4m 50s)",
        "assigned_practice_set_id": "DRILL-ROT-05Q",
        "practice_set_name": "5-Question Micro-Drill: Pivot Point Selection & Moment Arm Calculation",
        "remediation_duration_min": 30,
        "expected_score_lift_pct": 15.2
    },
    {
        "misconception_id": "MISC-CHEM-01",
        "surface_concept_id": "CONC-SN2-01",
        "surface_concept_name": "SN2 Bimolecular Nucleophilic Substitution",
        "root_cause_prerequisite_id": "CONC-CARB-01",
        "root_cause_prerequisite_name": "Carbocation Stability & Rearrangement",
        "prerequisite_gap_depth": 1,
        "misconception_description": "Assuming carbocation rearrangement occurs in single-step concerted bimolecular substitution.",
        "remediation_module_id": "MOD-CHEM-SN-03",
        "lecture_title": "Nucleophilic Substitution Mechanisms: Concerted vs Carbocation Pathways",
        "video_timestamp_range": "11:30 - 16:15 (4m 45s)",
        "assigned_practice_set_id": "DRILL-SN-05Q",
        "practice_set_name": "5-Question Micro-Drill: Walden Inversion vs Racemization Identification",
        "remediation_duration_min": 25,
        "expected_score_lift_pct": 15.0
    },
    {
        "misconception_id": "MISC-CHEM-02",
        "surface_concept_id": "CONC-CARB-01",
        "surface_concept_name": "Carbocation Stability & Rearrangement",
        "root_cause_prerequisite_id": "CONC-HYB-01",
        "root_cause_prerequisite_name": "Orbital Hybridization (sp3, sp2, sp)",
        "prerequisite_gap_depth": 2,
        "misconception_description": "Failing to recognize sp2 hybridization and empty p-orbital geometry of trivalent carbon.",
        "remediation_module_id": "MOD-CHEM-GOC-01",
        "lecture_title": "Organic Reaction Intermediates: Geometry and Energy Levels of Carbocations",
        "video_timestamp_range": "05:40 - 10:10 (4m 30s)",
        "assigned_practice_set_id": "DRILL-HYB-05Q",
        "practice_set_name": "5-Question Micro-Drill: Hydride Shifts & Hyperconjugative Stability",
        "remediation_duration_min": 20,
        "expected_score_lift_pct": 13.9
    },
    {
        "misconception_id": "MISC-MATH-01",
        "surface_concept_id": "CONC-MAX-01",
        "surface_concept_name": "Maxima, Minima & Optimization Derivatives",
        "root_cause_prerequisite_id": "CONC-CHAIN-01",
        "root_cause_prerequisite_name": "Chain Rule for Composite Differentiation",
        "prerequisite_gap_depth": 1,
        "misconception_description": "Omitting inner derivative multiplication when setting f'(x)=0 for composite functions.",
        "remediation_module_id": "MOD-MATH-CALC-06",
        "lecture_title": "Composite Function Derivatives: Mastering the Chain Rule in Optimization",
        "video_timestamp_range": "18:00 - 22:50 (4m 50s)",
        "assigned_practice_set_id": "DRILL-CHAIN-05Q",
        "practice_set_name": "5-Question Micro-Drill: Composite Critical Points and Second Derivative Test",
        "remediation_duration_min": 25,
        "expected_score_lift_pct": 15.6
    },
    {
        "misconception_id": "MISC-MATH-02",
        "surface_concept_id": "CONC-CHAIN-01",
        "surface_concept_name": "Chain Rule for Composite Differentiation",
        "root_cause_prerequisite_id": "CONC-FUNC-01",
        "root_cause_prerequisite_name": "Domain, Range & Composite Functions",
        "prerequisite_gap_depth": 2,
        "misconception_description": "Misidentifying outer vs inner function decomposition f(g(x)).",
        "remediation_module_id": "MOD-MATH-FUNC-02",
        "lecture_title": "Function Composition & Inverse Mappings: Structural Decomposition",
        "video_timestamp_range": "07:20 - 11:40 (4m 20s)",
        "assigned_practice_set_id": "DRILL-FUNC-05Q",
        "practice_set_name": "5-Question Micro-Drill: Step-by-Step Outer-Inner Layer Dissection",
        "remediation_duration_min": 20,
        "expected_score_lift_pct": 13.2
    }
]

remediation_df = pd.DataFrame(remediation_data)
remediation_df.to_csv(os.path.join(base_dir, "artifact 2.csv"), index=False)
print(f"✅ Created artifact 2.csv: {len(remediation_df)} curated misconception & remediation mappings.")

# ----------------------------------------------------------------------
# 3. GENERATE input 2.csv: Longitudinal Student Diagnostic Exam Logs
# ----------------------------------------------------------------------
# 150 students across 3 mock tests, with ~65% scoring <= 60%
first_names = ["Aarav", "Ananya", "Rohan", "Pooja", "Vikram", "Sneha", "Aditya", "Neha", "Rahul", "Priya",
               "Karthik", "Riya", "Arjun", "Kavya", "Siddharth", "Ishaan", "Tanvi", "Varun", "Meera", "Dev"]
last_names = ["Sharma", "Verma", "Patel", "Iyer", "Reddy", "Gupta", "Nair", "Mehta", "Singh", "Joshi",
              "Rao", "Choudhury", "Bose", "Pillai", "Das", "Bhat", "Deshmukh", "Kapoor", "Mukherjee", "Malhotra"]

students = []
student_id_counter = 1

# Specific clusters to map to
clusters = [
    {"cluster": "Mechanics - Newton's Laws & Friction", "surface_id": "CONC-NEWTON-03", "root_id": "CONC-FBD-01", "misc_id": "MISC-PHYS-01"},
    {"cluster": "Mechanics - Vector Force Projections", "surface_id": "CONC-FBD-01", "root_id": "CONC-VEC-01", "misc_id": "MISC-PHYS-02"},
    {"cluster": "Mechanics - Rotational Equilibrium", "surface_id": "CONC-ROT-01", "root_id": "CONC-NEWTON-02", "misc_id": "MISC-PHYS-03"},
    {"cluster": "Organic Chemistry - Substitution Mechanisms", "surface_id": "CONC-SN2-01", "root_id": "CONC-CARB-01", "misc_id": "MISC-CHEM-01"},
    {"cluster": "Organic Chemistry - Intermediate Stability", "surface_id": "CONC-CARB-01", "root_id": "CONC-HYB-01", "misc_id": "MISC-CHEM-02"},
    {"cluster": "Calculus - Optimization & Derivatives", "surface_id": "CONC-MAX-01", "root_id": "CONC-CHAIN-01", "misc_id": "MISC-MATH-01"},
    {"cluster": "Calculus - Composite Function Differentiation", "surface_id": "CONC-CHAIN-01", "root_id": "CONC-FUNC-01", "misc_id": "MISC-MATH-02"}
]

for i in range(150):
    stu_id = f"STU-2026-{student_id_counter:03d}"
    name = f"{random.choice(first_names)} {random.choice(last_names)}"
    exam = random.choice(["JEE Advanced 2026", "NEET 2026", "JEE Main 2026"])
    
    # Target score: 65% of students score <= 60%
    if i < 98: # 98 students (~65%) have score <= 60%
        score_pct = round(random.uniform(42.0, 60.0), 1)
        consec_fails = random.choice([2, 3, 3, 4])
        selected_cluster = clusters[i % len(clusters)]
    else:
        score_pct = round(random.uniform(61.0, 84.0), 1)
        consec_fails = random.choice([0, 1])
        selected_cluster = clusters[i % len(clusters)]
        
    mock_history = f"Mock-1: {round(score_pct - random.uniform(-2, 4), 1)}% | Mock-2: {round(score_pct - random.uniform(-1, 3), 1)}% | Mock-3: {score_pct}%"
    
    # Associated wrong question IDs
    matching_q = questions_df[questions_df["primary_concept_id"] == selected_cluster["surface_id"]]
    if len(matching_q) > 0:
        wrong_qs = ",".join(matching_q["question_id"].sample(min(3, len(matching_q)), random_state=i).tolist())
    else:
        wrong_qs = f"QSTN-PHYS-005,QSTN-PHYS-022,QSTN-PHYS-045"
        
    students.append({
        "student_id": stu_id,
        "student_name": name,
        "target_exam": exam,
        "latest_mock_score_pct": score_pct,
        "longitudinal_mock_history": mock_history,
        "persistent_concept_cluster": selected_cluster["cluster"],
        "surface_concept_id": selected_cluster["surface_id"],
        "consecutive_failure_count": consec_fails,
        "recent_wrong_question_ids": wrong_qs,
        "aggregate_misconception_id": selected_cluster["misc_id"],
        "student_study_hours_weekly": round(random.uniform(14.0, 28.0), 1)
    })
    student_id_counter += 1

students_df = pd.DataFrame(students)
students_df.to_csv(os.path.join(base_dir, "input 2.csv"), index=False)
print(f"✅ Created input 2.csv: {len(students_df)} student diagnostic logs. Mean score: {students_df['latest_mock_score_pct'].mean():.1f}%")
print("🎉 All 3 starting corpora generated successfully!")
