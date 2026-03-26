text = input("Enter your comment here: ").lower()
if "Make a lot of money" in text or "buy now" in text or "click this" in text:
    print("Alert!! This is spam comment!")
else:
    print("This isn't spam comment")
