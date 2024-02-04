#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Модуль для individual_task_1.py

def create_tagged_string(tag):
    def tag_string(content):
        return f"<{tag}>{content}</{tag}>"
    return tag_string
