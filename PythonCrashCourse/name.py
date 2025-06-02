name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"\tHello, {full_name.title()}!")
print(f"\nHello, {full_name.title()}!")
print(f"\n\tHello, {full_name.title()}!")
print(f"\t\nHello, {full_name.title()}!") #"\n" needs to come before "\t inorder achieve white space + new line, if "\n" is after then it overrides it"

#Stripping whitespace
favorite_language = "      python       "
print(favorite_language)
favorite_language = favorite_language.rstrip()     #Only removes the white spaces in front of it
print(favorite_language)
favorite_language = favorite_language.lstrip()     #Only removes the white space behind it
print(favorite_language)        
favorite_language = favorite_language.strip()      #Removes all the white spaces
print(favorite_language)
test = "   python   crash   course   "
test = test.strip()
print(test)          #strip doesn't remove all white spaces, just the beginning and end

#Removing prefixes
nostarch_url = "https://nostarch.com"
nostarch_url = nostarch_url.removeprefix("https://")     #removes prefixes
print(nostarch_url)
test2 = "https://google.com"
test2 = test2.removeprefix("google")
print(test2)
