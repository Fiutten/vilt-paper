from pathlib import Path
import re

p = Path('vilt.tex')
s = p.read_text(encoding='utf-8')
bs = chr(92)

s = s.replace(chr(7), bs)
s = s.replace(bs + 'bstract{', bs + 'abstract{')
s = s.replace(bs + 'cp{', bs + 'acp{')
s = s.replace(bs + 'c{', bs + 'ac{')

new_abs = (
    bs + 'abstract{Recent advances in ' + bs + 'ac{ai}, chatbots, and ' + bs + 'acp{llm} have created new opportunities for supporting students beyond the classroom. '
    'However, many LLM-based educational assistants remain general-purpose tools and are not explicitly grounded in the syllabus, materials, and pedagogical requirements of specific subjects. '
    'This paper presents ' + bs + 'ac{vilt}, a ' + bs + 'ac{rag} framework for deploying subject-specific LLM tutors in higher education. '
    + bs + 'ac{vilt} enables educators to provide course materials that are processed, indexed, and retrieved to generate answers aligned with each subject. '
    'The virtual tutor supports students by explaining concepts, providing examples, and answering subject-related questions, while structured prompts constrain its behavior to the available educational context. '
    'The framework also incorporates a feedback module and a learning analytics dashboard that summarizes student interactions through ' + bs + 'acp{kpi}, helping educators monitor system usage and identify topics that may require further reinforcement. '
    'An exploratory evaluation was conducted in subjects from three universities in Spain and Colombia. '
    'The results show the feasibility of deploying ' + bs + 'ac{vilt} across heterogeneous higher-education contexts and indicate positive perceptions from students and educators regarding its usefulness, precision, and pedagogical value.}'
)

s = re.sub(bs + 'abstract' + r'\{Recent advances.*?pedagogical value\.\}', lambda _: new_abs, s, count=1, flags=re.S)
p.write_text(s, encoding='utf-8')
print('vilt.tex header fixed')
