import re

with open("update_drill_dashboard.py") as f:
    code_db = f.read()

# Extract concept_drill_5q string
start_marker = "concept_drill_5q = {"
end_marker = "print(f\"Generated comprehensive question bank:"
idx_start = code_db.find(start_marker)
idx_end = code_db.find(end_marker)
drill_dict_code = code_db[idx_start:idx_end].strip()

with open("final output 3.py", "r") as f:
    orig = f.read()

# Replace concept_drill_db definition
orig_db_start = orig.find("# Curated Micro-Drill Question Database for All 7 Prerequisite Concepts")
orig_db_end = orig.find("# Foundational predecessor mappings for DAG breadcrumbs")

new_db_section = f"""# Curated Comprehensive 5-Question Drill Bank for All 7 Prerequisite Concepts
{drill_dict_code}
"""

updated = orig[:orig_db_start] + new_db_section + orig[orig_db_end:]

# In get_student_diagnostic_profile:
old_drill_data = 'drill_data = concept_drill_db.get(root_id, concept_drill_db["CONC-FBD-01"])'
new_drill_data = 'drill_questions = concept_drill_5q.get(root_id, concept_drill_5q["CONC-FBD-01"])'

updated = updated.replace(old_drill_data, new_drill_data)

# Replace the return dict in get_student_diagnostic_profile
old_ret = """"sample_q": drill_data["sample_q"],
        "sample_opts": drill_data["sample_opts"],
        "sample_ans": drill_data["sample_ans"],
        "explanation": drill_data["explanation"],"""

new_ret = """"drill_questions": drill_questions,"""

updated = updated.replace(old_ret, new_ret)

# Now update the expander in col_right
old_expander_start = updated.find("# Interactive Micro-Drill Quiz Simulator")
old_expander_end = updated.find("# TAB 2: COHORT ANALYTICS & ACADEMIC INTERVENTION OPERATIONS")

new_expander = """# Interactive Micro-Drill Quiz Simulator (All 5 Questions with Interactive Stepper)
        with st.expander(f"📝 Interactive Practice Drill: {active_student['drill_title']}", expanded=True):
            st.markdown(f"**Prerequisite Diagnostic Sequence** (Target: `{active_student['root_cause']}`):")
            
            # Interactive 5-Question Stepper Tabs
            drill_tabs = st.tabs(["Question 1", "Question 2", "Question 3", "Question 4", "Question 5"])
            for q_idx, tab in enumerate(drill_tabs):
                with tab:
                    q_obj = active_student["drill_questions"][q_idx]
                    st.markdown(f"**{q_obj['q']}**")
                    
                    user_choice = st.radio(
                        "Select Option:",
                        q_obj["opts"],
                        index=0,
                        key=f"q_{active_student['student_id']}_{q_idx}"
                    )
                    
                    c_q1, c_q2 = st.columns([1, 1.3])
                    with c_q1:
                        if st.button("🚀 Verify Question", key=f"btn_v_{active_student['student_id']}_{q_idx}", use_container_width=True, type="primary"):
                            st.session_state[f"verified_{active_student['student_id']}_{q_idx}"] = True
                    with c_q2:
                        if st.button("✅ Complete Full Drill", key=f"btn_comp_{active_student['student_id']}_{q_idx}", use_container_width=True):
                            st.session_state.remediation_completed = True
                            st.toast("🎉 Prerequisite Gap Remediation Recorded! Mastery updated to 92.5%.", icon="✅")
                            
                    if st.session_state.get(f"verified_{active_student['student_id']}_{q_idx}", False):
                        if user_choice == q_obj["ans"]:
                            st.success(f"✅ Correct! **{q_obj['ans']}** is the accurate result.")
                        else:
                            st.error(f"❌ Incorrect option selected. Correct answer: **{q_obj['ans']}**.")
                        st.info(f"💡 **Pedagogical Explanation**: {q_obj['expl']}")
                        
            if st.session_state.remediation_completed:
                st.success(f"🏆 Full 5-Question Drill Completed for `{active_student['student_id']}`! Projected Mock Score updated to **{min(active_student['score'] + active_student['expected_lift'], 95.0):.1f}%**.")


# ==============================================================================
"""

updated = updated[:old_expander_start] + new_expander + updated[old_expander_end:]

with open("final output 3.py", "w") as f:
    f.write(updated)

print("✅ Successfully updated final output 3.py with full 5-question stepper!")
