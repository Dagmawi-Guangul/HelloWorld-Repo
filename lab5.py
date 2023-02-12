
def DecodeWord(encodedWord):
    decodedWord = ""
    for i in encodedWord:
        if i == "t":
            decodedWord += "f"
        elif i == "f":
            decodedWord += "t"
        elif i == "3":
            decodedWord += "e"
        elif i == "k":
            decodedWord += "c"
        elif i == "z":
            decodedWord += "s"
        elif i == "b":
            decodedWord += "r"
        elif i == "x":
            decodedWord += "r"
        else:
            decodedWord += i
    return decodedWord

def main():
    encodedWord = "tx33dom"
    #encodedWord = "t3xb3f"
	#encodedWord = "koxb3zpond3nk3"
	#encodedWord = "fako fim3"
	#encodedWord = "zom3 xafz bun"	
	#encodedWord = "txiday tun tob tx3nkh tbi3z"
	#encodedWord = "kafz kan kafkh kakfuz3z wifh klawz"
	
	
	
	#encodedWord = "UUHO"  		#Used for Bonus
	#encodedWord = "EOUUUUOUU" 	#Used for Bonus
    print(DecodeWord(encodedWord))

if __name__ == "__main__":
    main()
