
def name_match(known_aliases, name):
    def middlename(n1, n2):
        if len(n1) > 1 and len(n2) > 1:
            return n1 == n2
        elif len(n1) == 1 and len(n2) > 1:
            return n1 == n2[0]
        elif len(n2) == 1 and len(n1) > 1:
            return n2 == n1[0]

    def match(alias, name):
        alias_parts = alias.split(' ')
        name_parts = name.split(' ')
        # middle name is missing
        if len(alias_parts) == 2:
            # known_aliases = ['Alphonse Capone']
            # just comparing first name and middle name in each alias_parts and name_parts
            return alias_parts[0] == name_parts[0] and alias_parts[-1] == name_parts[-1]
        # there's middlename
        elif len(alias_parts) == 3:
            # transponse only happens only when alias_parts has more than 3 elements
            # known_aliases = ['Alphonse Gabriel Capone']
            # name_match(known_aliases, 'Gabriel Alphonse Capone') => True
            # name_match(known_aliases, 'Gabriel A Capone') => True
            # name_match(known_aliases, 'Gabriel Capone') => True
            # name_match(known_aliases, 'Gabriel Francis Capone') => False

            # known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
            #name_match(known_aliases, 'Alphonse Gregory Capone') => False
            if alias_parts[0] != name_parts[0] or alias_parts[-1] != name_parts[-1]:
                return False
            if len(name_parts) == 3:
                # if alias_parts[1][0] != name_parts[1][0]:
                #     return False
                return middlename(alias_parts[1], name_parts[1])
        return True

    for alias in known_aliases:
        if match(alias, name):
            return True
        if len(alias.split(' ')) >= 3:
            alias = alias.split(' ')
            alias[0], alias[1] = alias[1], alias[0]
            alias = ' '.join(alias)
            if match(alias, name):
                print(True)
                return True
        return False
known_aliases = ['Alphonse Gabriel Capone', 'Al Capone']
name_match(known_aliases, 'Alphonse Gabriel Capone') #=> True
name_match(known_aliases, 'Al Capone') #=> True
name_match(known_aliases, 'Alphonse Francis Capone') #=> False
print('--------------------------')
known_aliases = ['Alphonse Capone']
name_match(known_aliases, 'Alphonse Gabriel Capone') #=> True
name_match(known_aliases, 'Alphonse Francis Capone') #=> True
name_match(known_aliases, 'Alexander Capone') #=> False
print('--------------------------')
known_aliases = ['Alphonse Gabriel Capone']
name_match(known_aliases, 'Alphonse Capone') #=> True
name_match(known_aliases, 'Alphonse Francis Capone') #=> False
name_match(known_aliases, 'Alexander Capone') #=> False
print('--------------------------')
known_aliases = ['Alphonse Gabriel Capone', 'Alphonse Francis Capone']
name_match(known_aliases, 'Alphonse Gabriel Capone') #=> True
name_match(known_aliases, 'Alphonse Francis Capone') #=> True
name_match(known_aliases, 'Alphonse Edward Capone') #=> False
print('--------------------------')
known_aliases = ['Alphonse Gabriel Capone', 'Alphonse F Capone']
name_match(known_aliases, 'Alphonse G Capone') #=> True
name_match(known_aliases, 'Alphonse Francis Capone') #=> True
name_match(known_aliases, 'Alphonse E Capone') #=> False
name_match(known_aliases, 'Alphonse Edward Capone') #=> False
name_match(known_aliases, 'Alphonse Gregory Capone') #=> False

known_aliases = ['Alphonse Gabriel Capone']
name_match(known_aliases, 'Gabriel Alphonse Capone') #=> True
name_match(known_aliases, 'Gabriel A Capone') #=> True
name_match(known_aliases, 'Gabriel Capone')# => True
print(name_match(known_aliases, 'Gabriel Francis Capone'))# => False