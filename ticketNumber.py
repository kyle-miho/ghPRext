import re

branchToTicket = {
    "lrqa" : "LRQA",
    "qa" : "LRQA",
    "lps" : "LPS",
}

class TicketNumber:
    def __formatTokens(self,tokens):
        if self.__validTokens(tokens):
            tokens[0] = re.sub('[^\w]','',tokens[0])
            tokens[0] = branchToTicket[tokens[0].lower()]

            tokens[1] = re.sub('[^0-9]','',tokens[1])  
        return tokens

    def __getNewTokens(self):
        offset = 0

        while (True):
            commit = getRecentCommit(offset).split(' ', 1)

            tokens = commit[0].split('-', 1)

            if self.__validTokens(tokens):
                return tokens
            elif offset > 10:
                sys.exit("Failed getting valid tokens")
            offset += 1

    def __tokenize(self,branch):
        tokens = branch.split("-")

        if len(tokens) == 3:
            tokens.pop(0)

        if self.__validTokens(tokens) == False:
            tokens = self.__getNewTokens()

        return self.__formatTokens(tokens)

    def __validTokens(self,tokens):
        if len(tokens) != 2:
            print('Wrong amount of tokens, expected 2. Tokens: ' + str(tokens))
            return False

        if tokens[0].lower() not in branchToTicket:
            print(tokens[0] + ' is not a valid branch name. Tokens: ' + str(tokens))
            return False

        if re.search("\d+",tokens[1]) == None:
            print(tokens[1] + ' should only contain digits. Tokens: ' + str(tokens))
            return False

        return True

    def __init__(self,branch):
        tokens = self.__tokenize(branch)      

        self.project = tokens[0]
        self.ticketNumber = tokens[1]

    def __str__(self):
        return self.project + "-" + self.ticketNumber