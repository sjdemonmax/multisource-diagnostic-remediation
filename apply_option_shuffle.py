import pprint

with open("final output 3.py", "r") as f:
    text = f.read()

start_str = "concept_drill_5q = {"
end_str = "# Foundational predecessor mappings for DAG breadcrumbs"

s_idx = text.find(start_str)
e_idx = text.find(end_str)

exec_dict = {}
exec(text[s_idx:e_idx], exec_dict)
drill_dict = exec_dict["concept_drill_5q"]

concept_patterns = [
    [1, 2, 0, 3, 1], # B, C, A, D, B
    [2, 0, 3, 1, 2], # C, A, D, B, C
    [3, 1, 2, 0, 3], # D, B, C, A, D
    [0, 3, 1, 2, 0], # A, D, B, C, A
    [1, 0, 2, 3, 2], # B, A, C, D, C
    [2, 3, 0, 1, 0], # C, D, A, B, A
    [3, 2, 1, 0, 1]  # D, C, B, A, B
]

for c_idx, (cid, q_list) in enumerate(drill_dict.items()):
    pattern = concept_patterns[c_idx % len(concept_patterns)]
    for q_idx, item in enumerate(q_list):
        t_idx = pattern[q_idx]
        cur_ans = item["ans"]
        cur_opts = list(item["opts"])
        ans_idx = cur_opts.index(cur_ans)
        cur_opts[ans_idx], cur_opts[t_idx] = cur_opts[t_idx], cur_opts[ans_idx]
        item["opts"] = cur_opts
        assert item["opts"][t_idx] == item["ans"]

# Format as clean Python code
formatted_code = "concept_drill_5q = {\n"
for cid, q_list in drill_dict.items():
    formatted_code += f'    "{cid}": [\n'
    for q in q_list:
        formatted_code += "        {\n"
        formatted_code += f'            "q": {repr(q["q"])},\n'
        formatted_code += f'            "opts": {repr(q["opts"])},\n'
        formatted_code += f'            "ans": {repr(q["ans"])},\n'
        formatted_code += f'            "expl": {repr(q["expl"])}\n'
        formatted_code += "        },\n"
    formatted_code = formatted_code.rstrip(",\n") + "\n    ],\n"
formatted_code = formatted_code.rstrip(",\n") + "\n}\n\n"

new_text = text[:s_idx] + formatted_code + text[e_idx:]

with open("final output 3.py", "w") as f:
    f.write(new_text)

print("✅ Successfully updated final output 3.py with realistic option distribution!")
