'''

  721. Merge Accounts

'''


def accountsMergeRef(accounts):
  parents     = {}
  emailToName = {}
  rootToRes   = {}
  
  # This find function returns its highest found parent in the node tree
    # If provided email is not highest found parent, then recursively go up tree
    # Return the highest found parent
  def find(email):
    nonlocal parents
    if email != parents[email]:
      parents[email] = find(parents[email])
    return parents[email]

  # This union function associates email with its highest found parent email
    # We use the find function for both email and parent email because the
    # parentEmail may also be a subcomponent of another tree node.
  def union(email, parentEmail):
    nonlocal parents
    parents[find(email)] = find(parentEmail)
    
  for account in accounts:
    name = account[0]

    for i in range(1, len(account)):
      email = account[i]
      if email not in parents: parents[email] = email
      emailToName[email] = name
      union(email, account[1])


  for email, name in emailToName.items():
    rootEmail = find(email)
    if rootEmail not in rootToRes: 
      rootToRes[rootEmail] = { "name": name, "emails": [] }
    rootToRes[rootEmail]["emails"].append(email)

  result = []
  for dict in rootToRes.values():
    result.append([[dict['name']] + sorted(dict['emails'])])

  return result

      
def accountsMerge(accounts):
  parents     = {}
  emailToName = {}
  rootToRes   = {}
  
  def find(node):
    if node != parents[node]:
      parents[node] = find(parents[node])
    return parents[node]

  def union(child, parent):
    parents[find(child)] = find(parent)

  for (name, *emails) in accounts:
    for email in emails:
      if email not in parents: parents[email] = email
      emailToName[email] = name
      union(email, emails[0])

  for email, name in emailToName.items():
    root = find(email)
    if root not in rootToRes: rootToRes[root] = {'name': name, 'emails': []}
    rootToRes[root]['emails'].append(email)
  
  result = []
  for dict in rootToRes.values():
    result.append([dict['name']] + sorted(dict['emails']))

  return result














print(accountsMerge([
  ["John","johnsmith@mail.com","john_newyork@mail.com"],
  ["John","johnsmith@mail.com","john00@mail.com"],
  ["Mary","mary@mail.com"],
  ["John","johnnybravo@mail.com"]
]))

print(accountsMerge([
  ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
  ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
  ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
  ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
  ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]
]))