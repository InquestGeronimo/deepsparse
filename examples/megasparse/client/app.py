# Copyright (c) 2021 - present / Neuralmagic, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from time import perf_counter

import streamlit as st
from settings import FeatureHandler as feat


# Titles
st.markdown(feat.title, unsafe_allow_html=True)
st.markdown(feat.subtitle, unsafe_allow_html=True)

# Sidebar
st.sidebar.selectbox(feat.tasks_desc, feat.tasks)
model_choice = st.sidebar.radio(feat.variants_desc, feat.variants.keys())
st.sidebar.markdown(feat.code_banner)
st.sidebar.code(body=feat.code_text, language=feat.language)
st.sidebar.markdown(feat.repo_test)

# Footer
st.markdown(feat.footer, unsafe_allow_html=True)

# Inference
for model_name, model in feat.variants.items():

    if model_choice == model_name:

        context = st.text_area(
            label=feat.example_context_label, height=150, value=feat.example_context
        )
        question = st.text_area(
            label=feat.example_question_label, value=feat.example_question
        )
        start = perf_counter()
        answer = model(question=question, context=context)
        end = perf_counter()
        infer_time = end - start
        infer_time = round(infer_time, 4)
        st.write(feat.answer_label, answer["answer"])
        st.write(infer_time, feat.time_label)
