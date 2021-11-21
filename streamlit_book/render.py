import streamlit as st

from .keywords import *
from .render_to_do_list import to_do_list_from_lines
from .render_true_or_false import true_or_false_from_lines
from .render_multiple_choice import render_multiple_choice
from .render_single_choice import render_single_choice
from .render_text_input import render_text_input
from .render_code_input import render_code_input
from .render_file_upload import render_file_upload

def render_file(fullpath):
    """
    Renders the file (it's always a file and not a folder)
    given the fullpath (path and filename).
    Only admits python or markdown, also by construction.
    """
    with open(fullpath) as fh:
        lines = fh.readlines()
        if fullpath.endswith(".py"):
            exec("".join(lines))
        elif fullpath.endswith(".md"):
            if lines[0].startswith(TODO_KEYWORD):
                to_do_list_from_lines(lines)
            elif lines[0].startswith(TRUE_FALSE_KEYWORD):
                true_or_false_from_lines(lines)
            elif lines[0].startswith(MULTIPLE_CHOICE_KEYWORD):
                render_multiple_choice(lines)
            elif lines[0].startswith(SINGLE_CHOICE_KEYWORD):
                render_single_choice(lines)
            elif lines[0].startswith(CODE_INPUT_KEYWORD):
                render_code_input(lines)
            elif lines[0].startswith(TEXT_INPUT_KEYWORD):
                render_text_input(lines)
            elif lines[0].startswith(FILE_UPLOAD_KEYWORD):
                render_file_upload(lines)
            else:
                st.markdown("".join(lines), unsafe_allow_html=True)
        else:
            st.warning("File not supported")