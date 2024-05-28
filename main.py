import os
import commands
import Playground
import select_llm_details

print("Change LLM settings, Y or N?")

thing = input("").strip().upper()

if thing == "Y":
    select_llm_details.run_llm_settings()

Playground.Main().init("protagonist.json")