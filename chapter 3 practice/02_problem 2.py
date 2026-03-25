letter = """Dear
   <|Name|>,
    You are selected!
     <|Date|>"""
print(
    letter.replace("<|Name|>", "Safin Mahmud").replace("<|Date|>", "25-Mar-26")
)
