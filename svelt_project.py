from bs4 import BeautifulSoup
import requests


def find_meaning(word):
	
	url= f'https://www.dictionary.com/browse/{word}'
	html_text = requests.get(url).text
	soup = BeautifulSoup( html_text, 'lxml')

	meanings= soup.find_all('span', class_='one-click-content css-nnyc96 e1q3nk1v1')
	return meanings

while True:
        print('___DICTOINARY___')
        print('1.Find The Meaning of a word')
        print('2.Exit')
        x=int(input('choose an option:'))
        if x==2:
                break
        elif x==1:
                word1=input('enter the word:')
                meaning_list = find_meaning(word1)
                flag=0
                print(meaning_list[flag].text)
                while True:
                        more=input('want another meaning?(Y/N)')
                        if more in 'Yy':
                                try:
                                        flag+=1
                                        print(meaning_list[flag].text)
                                        print('')
                                except:
                                        print('no more synonyms left')
				
                        elif more in 'Nn':
                                break
				
                        else:
                                print('invalid input')
                                pass
		#break
        else:
                print('invalid input')
                pass




