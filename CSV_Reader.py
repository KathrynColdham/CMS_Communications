import pandas as pd
import matplotlib.pyplot as plt
 
df = pd.read_csv("CMSInternalCommunicationsFeedbackForm.csv", index_col=0)

Column4Count = df['4. If you are not resident at CERN, in which country are you based?'].value_counts()
Column5Count = df['5. In which country is your home institute, if different from the country in which you are based?'].value_counts()
Column8Count = df['8. If you answered "other" for question 7, please list the area(s) of CMS that you are involved in here.'].value_counts()
Column14Count = df['14. If you answered "other" for question 13, please provide the name of the platform(s) you use and the name of the announcement(s) you use it for. If you did not answer "other", please write "N/A" for this question.'].value_counts()


print('4. If you are not resident at CERN, in which country are you based?')
print('')
print(Column4Count)
print('')
print('5. In which country is your home institute, if different from the country in which you are based?')
print('')
print(Column5Count)
print('8. If you answered "other" for question 7, please list the area(s) of CMS that you are involved in here.')
print('')
print(Column8Count)
print('')
print('14. If you answered "other" for question 13, please provide the name of the platform(s) you use and the name of the announcement(s) you use it for. If you did not answer "other", please write "N/A" for this question.')

Column4Count.plot.bar()
plt.title("4. Country based in (if not resident at CERN)")
plt.xlabel("Country")
plt.xticks(size = 4.5)
plt.ylabel("Number of responses")
plt.savefig('Question4_CountryBased_NotResidentAtCERN.pdf')
plt.show()

Column5Count.plot.bar()
plt.title("5. Country of home institute (if different from country based in)")
plt.xlabel("Country")
plt.xticks(size = 4.5)
plt.ylabel("Number of responses")
plt.savefig('Question5_HomeInstituteCountry_DifferentFromCountryBased.pdf')
plt.show()

Column8Count.plot.bar()
plt.title("8. Area of CMS involved in (if not listed in question 7)")
plt.xlabel("Area")
plt.xticks(size = 3)
plt.ylabel("Number of responses")
plt.savefig('Question8_AreaOfCMS.pdf')
plt.show()

Column14Count.plot.bar()
plt.title("14. Platform used and name of announcement")
plt.xlabel("Platform and announcement")
plt.xticks(size = 3)
plt.ylabel("Number of responses")
plt.savefig('Question14_PlatformAndAnnouncement.pdf')
plt.show()

