import pandas as pd
import matplotlib.pyplot as plt
import argparse

df = pd.read_csv("CMSInternalCommunicationsFeedbackForm.csv", index_col=0)


#x = raw_input("\033[1m" + 'Which column would you like to obtain a subset of? ' + "\033[0m")
#print 'The chosen column is ' + x
#print('')

#y = raw_input("\033[1m" + 'What value would you like for entries in this subset to be equal to? ' + "\033[0m")
#print 'The chosen value is ' + y
#print('')

#z = raw_input("\033[1m" + 'Which column for rows in this subset would you like to plot? ' + "\033[0m")
#print 'The chosen column for plotting is ' + z

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--subset", type=str, help="title of column to take a subset of rows of")

parser.add_argument("-c", "--content", type=str, help="cell content wanted")

parser.add_argument("-p", "--plot", type=str, help="title of column to plot")

args = parser.parse_args()

x = args.subset
y = args.content
z = args.plot

#Chosen column to filter a subset
if x == '1. For how many years have you been a member of the CMS collaboration?':
	x_column_subset = ' CMS membership'
	pdf_string1 = 'CMSMembership'
elif x == '2. In which age range do you fall under?':
	x_column_subset = ' age '
	pdf_string1 = "Age"
elif x == '3. Are you currently resident (>50%) at CERN?':
	x_column_subset = ' % presence at CERN '
	pdf_string1 = "CERNPercentagePresence"
elif x == '4. If you are not resident at CERN, in which country are you based?':
	x_column_subset = 'based in '
	pdf_string1 = "CountryBasedIn"
elif x == '5. In which country is your home institute, if different from the country in which you are based?':
	x_column_subset = ' home institute in '
	pdf_string1 = "HomeInstituteIn"
elif x == '6. Approximately, what was your percentage of presence at CERN before the COVID-19 pandemic began?':
	x_column_subset = ' CERN presence (pre-COVID) '
	pdf_string1 = "PercentageOfPresenceAtCERNBeforeCOVID"
elif x == '7. Which of the following areas of CMS are you involved in? ':
	x_column_subset = ' CMS area involved in '
	pdf_string1 = "CMSArea"
else:
	print('ERROR: Please check chosen column name for the column you would like to choose a subset of.')



#Subset value
if y == '< 1':
	x_column_subset_value = ' < 1 year.'
        pdf_string2 = '_LessThan1Year_'
elif y == '1-2':
        x_column_subset_value = ' 1-2 years.'
        pdf_string2 = '_1To2Years_'
elif y == '3-5':
        x_column_subset_value = ' 3-5 years.'
        pdf_string2 = '_3To5Years_'
elif y == '6-10':
        x_column_subset_value = ' 6-10 years.'
        pdf_string2 = '_6To10Years_'
elif y == '10+':
	x_column_subset_value = ' 10+ years.'
	pdf_string2 = '_10PlusYears_'
elif y == '18-25':
	x_column_subset_value = ' 18-25 years old'
	pdf_string2 = "_18To25Years_"
elif y == '26-35':
        x_column_subset_value = ' 26-35 years old'
        pdf_string2 = "_26To35Years_"
elif y == '36-45':
        x_column_subset_value = ' 36-45 years old'
        pdf_string2 = "_36To45Years_"
elif y == '46-55':
        x_column_subset_value = ' 46-55 years old'
        pdf_string2 = "_46To55Years_"
elif y == '56-65':
        x_column_subset_value = ' 56-65 years old'
        pdf_string2 = "_56To65Years_"
elif y == '66-75':
        x_column_subset_value = ' 66-75 years old'
        pdf_string2 = "_66To75Years_"
elif y == '75+':
        x_column_subset_value = ' 75+ years old'
        pdf_string2 = "_75YearsOrOver_"
elif y == 'Yes':
	x_column_subset_value = ' >50%'
	pdf_string2 = '_PresenceAtCERNGreaterThan50%_'
elif y == 'No':
        x_column_subset_value = ' <=50%'
        pdf_string2 = '_PresenceAtCERNLessThanOrEqual50%_'
elif y == 'Afghanistan':
	x_column_subset_value = 'Afghanistan'
	pdf_string2 = '_Afghanistan_'
elif y == 'Albania':
        x_column_subset_value = 'Albania'
        pdf_string2 = '_Albania_'
elif y == 'Algeria':
        x_column_subset_value = 'Algeria'
        pdf_string2 = '_Algeria_'
elif y == 'Andorra':
        x_column_subset_value = 'Andorra'
        pdf_string2 = '_Andorra_'
elif y == 'Angola':
        x_column_subset_value = 'Angola'
        pdf_string2 = '_Angola_'
elif y == 'Antigua and Barbuda':
        x_column_subset_value = 'Antigua and Barbuda'
        pdf_string2 = '_AntiguaAndBarbuda_'
elif y == 'Argentina':
        x_column_subset_value = 'Argentina'
        pdf_string2 = '_Argentina_'
elif y == 'Armenia':
        x_column_subset_value = 'Armenia'
        pdf_string2 = '_Armenia_'
elif y == 'Australia':
        x_column_subset_value = 'Australia'
        pdf_string2 = '_Australia_'
elif y == 'Austria':
        x_column_subset_value = 'Austria'
        pdf_string2 = '_Austria_'
elif y == 'Azerbaijan':
        x_column_subset_value = 'Azerbaijan'
        pdf_string2 = '_Azerbaijan_'
elif y == 'Bahamas':
        x_column_subset_value = 'Bahamas'
        pdf_string2 = '_Bahamas_'
elif y == 'Bahrain':
        x_column_subset_value = 'Bahrain'
        pdf_string2 = '_Bahrain_'
elif y == 'Bangladesh':
        x_column_subset_value = 'Bangladesh'
        pdf_string2 = '_Bangladesh_'
elif y == 'Barbados':
        x_column_subset_value = 'Barbados'
        pdf_string2 = '_Barbados_'
elif y == 'Belarus':
        x_column_subset_value = 'Belarus'
        pdf_string2 = '_Belarus_'
elif y == 'Belgium':
        x_column_subset_value = 'Belgium'
        pdf_string2 = '_Belgium_'
elif y == 'Belize':
        x_column_subset_value = 'Belize'
        pdf_string2 = '_Belize_'
elif y == 'Benin':
        x_column_subset_value = 'Benin'
        pdf_string2 = '_Benin_'
elif y == 'Bhutan':
        x_column_subset_value = 'Bhutan'
        pdf_string2 = '_Bhutan_'
elif y == 'Bolivia':
        x_column_subset_value = 'Bolivia'
        pdf_string2 = '_Bolivia_'
elif y == 'Bosnia and Herzegovina':
        x_column_subset_value = 'Bosnia and Herzegovina'
        pdf_string2 = '_BosinaAndHerzegovina_'
elif y == 'Botswana':
        x_column_subset_value = 'Botswana'
        pdf_string2 = '_Botswana_'
elif y == 'Brazil':
        x_column_subset_value = 'Brazil'
        pdf_string2 = '_Brazil_'
elif y == 'Brunei':
        x_column_subset_value = 'Brunei'
        pdf_string2 = '_Brunei_'
elif y == 'Bulgaria':
        x_column_subset_value = 'Bulgaria'
        pdf_string2 = '_Bulgaria_'
elif y == 'Burkina Faso':
        x_column_subset_value = 'Burkina Faso'
        pdf_string2 = '_BurkinaFaso_'
elif y == 'Burundi':
        x_column_subset_value = 'Burundi'
        pdf_string2 = '_Burundi_'
elif y == 'Cabo Verde':
        x_column_subset_value = 'Cabo Verde'
        pdf_string2 = '_CaboVerde_'
elif y == 'Cambodia':
        x_column_subset_value = 'Cambodia'
        pdf_string2 = '_Cambodia_'
elif y == 'Cameroon':
        x_column_subset_value = 'Cameroon'
        pdf_string2 = '_Cameroon_'
elif y == 'Canada':
        x_column_subset_value = 'Canada'
        pdf_string2 = '_Canada_'
elif y == 'Central African Republic':
        x_column_subset_value = 'Central African Republic'
        pdf_string2 = '_CentralAfricanRepublic_'
elif y == 'Chad':
        x_column_subset_value = 'Chad'
        pdf_string2 = '_Chad_'
elif y == 'Chile':
        x_column_subset_value = 'Chile'
        pdf_string2 = '_Chile_'
elif y == 'China':
        x_column_subset_value = 'China'
        pdf_string2 = '_China_'
elif y == 'Colombia':
        x_column_subset_value = 'Colombia'
        pdf_string2 = '_Colombia_'
elif y == 'Comoros':
        x_column_subset_value = 'Comoros'
        pdf_string2 = '_Comoros_'
elif y == 'Congo':
        x_column_subset_value = 'Congo, Democratic Republic of the'
        pdf_string2 = '_DRCongo_'
elif y == 'Costa Rica':
        x_column_subset_value = 'Costa Rica'
        pdf_string2 = '_CostaRica_'
elif y == 'Croatia':
        x_column_subset_value = 'Croatia'
        pdf_string2 = '_Croatia_'
elif y == 'Cuba':
        x_column_subset_value = 'Cuba'
        pdf_string2 = '_Cuba_'
elif y == 'Cyprus':
        x_column_subset_value = 'Cyprus'
        pdf_string2 = '_Cyprus_'
elif y == 'Czech Republic':
        x_column_subset_value = 'Czech Republic'
        pdf_string2 = '_CzechRepublic_'
elif y == 'Denmark':
        x_column_subset_value = 'Denmark'
        pdf_string2 = '_Denmark_'
elif y == 'Djibouti':
        x_column_subset_value = 'Djibouti'
        pdf_string2 = '_Djibouti_'
elif y == 'Dominica':
        x_column_subset_value = 'Dominica'
        pdf_string2 = '_Dominica_'
elif y == 'Dominican Republic':
        x_column_subset_value = 'Dominican Republic'
        pdf_string2 = '_DominicanRepublic_'
elif y == 'East Timor (Timor-Leste)':
        x_column_subset_value = 'East Timor (Timor-Leste)'
        pdf_string2 = '_EastTimor_'
elif y == 'Ecuador':
        x_column_subset_value = 'Ecuador'
        pdf_string2 = '_Ecuador_'
elif y == 'Egypt':
        x_column_subset_value = 'Egypt'
        pdf_string2 = '_Egypt_'
elif y == 'El Salvador':
        x_column_subset_value = 'El Salvador'
        pdf_string2 = '_ElSalvador_'
elif y == 'Equatorial Guinea':
        x_column_subset_value = 'Equatorial Guinea'
        pdf_string2 = '_EquatorialGuinea_'
elif y == 'Eritrea':
        x_column_subset_value = 'Eritrea'
        pdf_string2 = '_Eritrea_'
elif y == 'Estonia':
        x_column_subset_value = 'Estonia'
        pdf_string2 = '_Estonia_'
elif y == 'Eswatini':
        x_column_subset_value = 'Eswatini'
        pdf_string2 = '_Eswatini_'
elif y == 'Ethiopia':
        x_column_subset_value = 'Ethiopia'
        pdf_string2 = '_Ethiopia_'
elif y == 'Fiji':
        x_column_subset_value = 'Fiji'
        pdf_string2 = '_Fiji_'
elif y == 'Finland':
        x_column_subset_value = 'Finland'
        pdf_string2 = '_Finland_'
elif y == 'France':
        x_column_subset_value = 'France'
        pdf_string2 = '_France_'
elif y == 'Gabon':
        x_column_subset_value = 'Gabon'
        pdf_string2 = '_Gabon_'
elif y == 'The Gambia':
        x_column_subset_value = 'The Gambia'
        pdf_string2 = '_TheGambia_'
elif y == 'Georgia':
        x_column_subset_value = 'Georgia'
        pdf_string2 = '_Georgia_'
elif y == 'Germany':
        x_column_subset_value = 'Germany'
        pdf_string2 = '_Germany_'
elif y == 'Ghana':
        x_column_subset_value = 'Ghana'
        pdf_string2 = '_Ghana_'
elif y == 'Greece':
        x_column_subset_value = 'Greece'
        pdf_string2 = '_Greece_'
elif y == 'Grenada':
        x_column_subset_value = 'Grenada'
        pdf_string2 = '_Grenada_'
elif y == 'Guatemala':
        x_column_subset_value = 'Guatemala'
        pdf_string2 = '_Guatemala_'
elif y == 'Guinea':
        x_column_subset_value = 'Guinea'
        pdf_string2 = '_Guinea_'
elif y == 'Guinea-Bissau':
        x_column_subset_value = 'Guinea-Bissau'
        pdf_string2 = '_GuineaBissau_'
elif y == 'Guyana':
        x_column_subset_value = 'Guyana'
        pdf_string2 = '_Guyana_'
elif y == 'Haiti':
        x_column_subset_value = 'Haiti'
        pdf_string2 = '__Haiti'
elif y == 'Honduras':
        x_column_subset_value = 'Honduras'
        pdf_string2 = '_Honduras_'
elif y == 'Hungary':
        x_column_subset_value = 'Hungary'
        pdf_string2 = '_Hungary_'
elif y == 'Iceland':
        x_column_subset_value = 'Iceland'
        pdf_string2 = '_Iceland_'
elif y == 'India':
        x_column_subset_value = 'India'
        pdf_string2 = '_India_'
elif y == 'Indonesia':
        x_column_subset_value = 'Indonesia'
        pdf_string2 = '_Indonesia_'
elif y == 'Iran':
        x_column_subset_value = 'Iran'
        pdf_string2 = '_Iran_'
elif y == 'Iraq':
        x_column_subset_value = 'Iraq'
        pdf_string2 = '_Iraq_'
elif y == 'Ireland':
        x_column_subset_value = 'Ireland'
        pdf_string2 = '_Ireland_'
elif y == 'Israel':
        x_column_subset_value = 'Israel'
        pdf_string2 = '_Israel_'
elif y == 'Italy':
        x_column_subset_value = 'Italy'
        pdf_string2 = '_Italy_'
elif y == 'Jamaica':
        x_column_subset_value = 'Jamaica'
        pdf_string2 = '_Jamaica_'
elif y == 'Japan':
        x_column_subset_value = 'Japan'
        pdf_string2 = '_Japan_'
elif y == 'Jordan':
        x_column_subset_value = 'Jordan'
        pdf_string2 = '_Jordan_'
elif y == 'Kazakhstan':
        x_column_subset_value = 'Kazakhstan'
        pdf_string2 = '_Kazakhstan_'
elif y == 'Kenya':
        x_column_subset_value = 'Kenya'
        pdf_string2 = '_Kenya_'
elif y == 'Kiribati':
        x_column_subset_value = 'Kiribati'
        pdf_string2 = '_Kiribati_'
elif y == 'Korea,North':
        x_column_subset_value = 'Korea,North'
        pdf_string2 = '_NorthKorea_'
elif y == 'Korea,South':
        x_column_subset_value = 'Korea,South'
        pdf_string2 = '_SouthKorea_'
elif y == 'Kosovo':
        x_column_subset_value = 'Kosovo'
        pdf_string2 = '_Kosovo_'
elif y == 'Kuwait':
        x_column_subset_value = 'Kuwait'
        pdf_string2 = '_Kuwait_'
elif y == 'Kyrgyzstan':
        x_column_subset_value = 'Kyrgyzstan'
        pdf_string2 = '_Kyrgyzstan_'
elif y == 'Laos':
        x_column_subset_value = 'Laos'
        pdf_string2 = '_Laos_'
elif y == 'Latvia':
        x_column_subset_value = 'Latvia'
        pdf_string2 = '_Latvia_'
elif y == 'Lebanon':
        x_column_subset_value = 'Lebanon'
        pdf_string2 = '_Lebanon_'
elif y == 'Lesotho':
        x_column_subset_value = 'Lesotho'
        pdf_string2 = '_Lesotho_'
elif y == 'Liberia':
        x_column_subset_value = 'Liberia'
        pdf_string2 = '_Liberia_'
elif y == 'Libya':
        x_column_subset_value = 'Libya'
        pdf_string2 = '_Libya_'
elif y == 'Liechtenstein':
        x_column_subset_value = 'Liechtenstein'
        pdf_string2 = '_Liechtenstein_'
elif y == 'Lithuania':
        x_column_subset_value = 'Lithuania'
        pdf_string2 = '_Lithuania_'
elif y == 'Luxembourg':
        x_column_subset_value = 'Luxembourg'
        pdf_string2 = '_Luxembourg_'
elif y == 'Madagascar':
        x_column_subset_value = 'Madagascar'
        pdf_string2 = '_Madagascar_'
elif y == 'Malawi':
        x_column_subset_value = 'Malawi'
        pdf_string2 = '_Malawi_'
elif y == 'Malaysia':
        x_column_subset_value = 'Malaysia'
        pdf_string2 = '_Malaysia_'
elif y == 'Maldives':
        x_column_subset_value = 'Maldives'
        pdf_string2 = '_Maldives_'
elif y == 'Mali':
        x_column_subset_value = 'Mali'
        pdf_string2 = '_Mali_'
elif y == 'Malta':
        x_column_subset_value = 'Malta'
        pdf_string2 = '_Malta_'
elif y == 'Marshall Islands':
        x_column_subset_value = 'Marshall Islands'
        pdf_string2 = '_MarshallIslands_'
elif y == 'Mauritania':
        x_column_subset_value = 'Mauritania'
        pdf_string2 = '_Mauritania_'
elif y == 'Mauritius':
        x_column_subset_value = 'Mauritius'
        pdf_string2 = '_Mauritius_'
elif y == 'Mexico':
        x_column_subset_value = 'Mexico'
        pdf_string2 = '_Mexico_'
elif y == 'Micronesia, Federated States of':
        x_column_subset_value = 'Micronesia, Federated States of'
        pdf_string2 = '_FederatedStatesOfMicronesia_'
elif y == 'Moldova':
        x_column_subset_value = 'Moldova'
        pdf_string2 = '_Moldova_'
elif y == 'Monaco':
        x_column_subset_value = 'Monaco'
        pdf_string2 = '_Monaco_'
elif y == 'Mongolia':
        x_column_subset_value = 'Mongolia'
        pdf_string2 = '_Mongolia_'
elif y == 'Montenegro':
        x_column_subset_value = 'Montenegro'
        pdf_string2 = '_Montenegro_'
elif y == 'Morocco':
        x_column_subset_value = 'Morocco'
        pdf_string2 = '_Morocco_'
elif y == 'Mozambique':
        x_column_subset_value = 'Mozambique'
        pdf_string2 = '_Mozambique_'
elif y == 'Myanmar (Burma)':
        x_column_subset_value = 'Myanmar (Burma)'
        pdf_string2 = '_Myanmar_'
elif y == 'Namibia':
        x_column_subset_value = 'Namibia'
        pdf_string2 = '_Namibia_'
elif y == 'Nauru':
        x_column_subset_value = 'Nauru'
        pdf_string2 = '_Nauru_'
elif y == 'Nepal':
        x_column_subset_value = 'Nepal'
        pdf_string2 = '_Nepal_'
elif y == 'Netherlands':
        x_column_subset_value = 'Netherlands'
        pdf_string2 = '_Netherlands_'
elif y == 'NewZealand':
        x_column_subset_value = 'NewZealand'
        pdf_string2 = '_NewZealand_'
elif y == 'Nicaragua':
        x_column_subset_value = 'Nicaragua'
        pdf_string2 = '_Nicaragua_'
elif y == 'Niger':
        x_column_subset_value = 'Niger'
        pdf_string2 = '_Niger_'
elif y == 'North Macedonia':
        x_column_subset_value = 'North Macedonia'
        pdf_string2 = '_NorthMacedonia_'
elif y == 'Norway':
        x_column_subset_value = 'Norway'
        pdf_string2 = '_Norway_'
elif y == 'Oman':
        x_column_subset_value = 'Oman'
        pdf_string2 = '_Oman_'
elif y == 'Pakistan':
        x_column_subset_value = 'Pakistan'
        pdf_string2 = '_Pakistan_'
elif y == 'Palau':
        x_column_subset_value = 'Palau'
        pdf_string2 = '_Palau_'
elif y == 'Panama':
        x_column_subset_value = 'Panama'
        pdf_string2 = '_Panama_'
elif y == 'Papua New Guinea':
        x_column_subset_value = 'Papua New Guinea'
        pdf_string2 = '_PapuaNewGuinea_'
elif y == 'Paraguay':
        x_column_subset_value = 'Paraguay'
        pdf_string2 = '_Paraguay_'
elif y == 'Peru':
        x_column_subset_value = 'Peru'
        pdf_string2 = '_Peru_'
elif y == 'Philippines':
        x_column_subset_value = 'Philippines'
        pdf_string2 = '_Philippines_'
elif y == 'Poland':
        x_column_subset_value = 'Poland'
        pdf_string2 = '_Poland_'
elif y == 'Portugal':
        x_column_subset_value = 'Portugal'
        pdf_string2 = '_Portugal_'
elif y == 'Qatar':
        x_column_subset_value = 'Qatar'
        pdf_string2 = '_Qatar_'
elif y == 'Romania':
        x_column_subset_value = 'Romania'
        pdf_string2 = '_Romania_'
elif y == 'Russia':
        x_column_subset_value = 'Russia'
        pdf_string2 = '_Russia_'
elif y == 'Rwanda':
        x_column_subset_value = 'Rwanda'
        pdf_string2 = '_Rwanda_'
elif y == 'Saint Kitts and Nevis':
        x_column_subset_value = 'Saint Kitts and Nevis'
        pdf_string2 = '_SaintKittsandNevis_'
elif y == 'Saint Lucia':
        x_column_subset_value = 'Saint Lucia'
        pdf_string2 = '_SaintLucia_'
elif y == 'Saint Vincent and the Grenadines':
        x_column_subset_value = 'Saint Vincent and the Grenadines'
        pdf_string2 = '_SaintVincentAndTheGrenadines_'
elif y == 'Samoa':
        x_column_subset_value = 'Samoa'
        pdf_string2 = '_Samoa_'
elif y == 'San Marino':
        x_column_subset_value = 'San Marino'
        pdf_string2 = '_SanMarino_'
elif y == 'Sao Tome and Principe':
        x_column_subset_value = 'Sao Tome and Principe'
        pdf_string2 = '_SaoTomeAndPrincipe_'
elif y == 'Saudi Arabia':
        x_column_subset_value = 'Saudi Arabia'
        pdf_string2 = '_SaudiArabia_'
elif y == 'Senegal':
        x_column_subset_value = 'Senegal'
        pdf_string2 = '_Senegal_'
elif y == 'Serbia':
        x_column_subset_value = 'Serbia'
        pdf_string2 = '_Serbia_'
elif y == 'Seychelles':
        x_column_subset_value = 'Seychelles'
        pdf_string2 = '_Seychelles_'
elif y == 'Sierra Leone':
        x_column_subset_value = 'Sierra Leone'
        pdf_string2 = '_SierraLeone_'
elif y == 'Singapore':
        x_column_subset_value = 'Singapore'
        pdf_string2 = '_Singapore_'
elif y == 'Slovakia':
        x_column_subset_value = 'Slovakia'
        pdf_string2 = '_Slovakia_'
elif y == 'Slovenia':
        x_column_subset_value = 'Slovenia'
        pdf_string2 = '_Slovenia_'
elif y == 'Solomon Islands':
        x_column_subset_value = 'Solomon Islands'
        pdf_string2 = '_SolomonIslands_'
elif y == 'Somalia':
        x_column_subset_value = 'Somalia'
        pdf_string2 = '_Somalia_'
elif y == 'South Africa':
        x_column_subset_value = 'South Africa'
        pdf_string2 = '_SouthAfrica_'
elif y == 'Spain':
        x_column_subset_value = 'Spain'
        pdf_string2 = '_Spain_'
elif y == 'Sri Lanka':
        x_column_subset_value = 'Sri Lanka'
        pdf_string2 = '_SriLanka_'
elif y == 'Sudan':
        x_column_subset_value = 'Sudan'
        pdf_string2 = '_Sudan_'
elif y == 'Sudan,South':
        x_column_subset_value = 'Sudan,South'
        pdf_string2 = '_SouthSudan_'
elif y == 'Suriname':
        x_column_subset_value = 'Suriname'
        pdf_string2 = '_Suriname_'
elif y == 'Sweden':
        x_column_subset_value = 'Sweden'
        pdf_string2 = '_Sweden_'
elif y == 'Switzerland':
        x_column_subset_value = 'Switzerland'
        pdf_string2 = '_Switzerland_'
elif y == 'Syria':
        x_column_subset_value = 'Syria'
        pdf_string2 = '_Syria_'
elif y == 'Taiwan':
        x_column_subset_value = 'Taiwan'
        pdf_string2 = '_Taiwan_'
elif y == 'Tajikistan':
        x_column_subset_value = 'Tajikistan'
        pdf_string2 = '_Tajikistan_'
elif y == 'Tanzania':
        x_column_subset_value = 'Tanzania'
        pdf_string2 = '_Tanzania_'
elif y == 'Thailand':
        x_column_subset_value = 'Thailand'
        pdf_string2 = '_Thailand_'
elif y == 'Togo':
        x_column_subset_value = 'Togo'
        pdf_string2 = '_Togo_'
elif y == 'Tonga':
        x_column_subset_value = 'Tonga'
        pdf_string2 = '_Tonga_'
elif y == 'Trinidad and Tobago':
        x_column_subset_value = 'Trinidad and Tobago'
        pdf_string2 = '_TrinidadAndTobago_'
elif y == 'Tunisia':
        x_column_subset_value = 'Tunisia'
        pdf_string2 = '_Tunisia_'
elif y == 'Turkey':
        x_column_subset_value = 'Turkey'
        pdf_string2 = '_Turkey_'
elif y == 'Turkmenistan':
        x_column_subset_value = 'Turkmenistan'
        pdf_string2 = '_Turkmenistan_'
elif y == 'Tuvalu':
        x_column_subset_value = 'Tuvalu'
        pdf_string2 = '_Tuvalu_'
elif y == 'Uganda':
        x_column_subset_value = 'Uganda'
        pdf_string2 = '_Uganda_'
elif y == 'Ukraine':
        x_column_subset_value = 'Ukraine'
        pdf_string2 = '_Ukraine_'
elif y == 'United Arab Emirates':
        x_column_subset_value = 'United Arab Emirates'
        pdf_string2 = '_UnitedArabEmirates_'
elif y == 'United Kingdom':
        x_column_subset_value = 'United Kingdom'
        pdf_string2 = '_UnitedKingdom_'
elif y == 'United States':
        x_column_subset_value = 'United States'
        pdf_string2 = '_UnitedStates_'
elif y == 'Uruguay':
        x_column_subset_value = 'Uruguay'
        pdf_string2 = '_Uruguay_'
elif y == 'Uzbekistan':
        x_column_subset_value = 'Uzbekistan'
        pdf_string2 = '_Uzbekistan_'
elif y == 'Vanuatu':
        x_column_subset_value = 'Vanuatu'
        pdf_string2 = '_Vanuatu_'
elif y == 'Vatican City':
        x_column_subset_value = 'Vatican City'
        pdf_string2 = '_VaticanCity_'
elif y == 'Venezuela':
        x_column_subset_value = 'Venezuela'
        pdf_string2 = '_Venezuela_'
elif y == 'Vietnam':
        x_column_subset_value = 'Vietnam'
        pdf_string2 = '_Vietnam_'
elif y == 'Yemen':
        x_column_subset_value = 'Yemen'
        pdf_string2 = '_Yemen_'
elif y == 'Zambia':
        x_column_subset_value = 'Zambia'
        pdf_string2 = '_Zambia_'
elif y == 'Zimbabwe':
        x_column_subset_value = 'Zimbabwe'
        pdf_string2 = '_Zimbabwe_'
elif y == '0-10%':
	x_column_subset_value = '0-10%'
        pdf_string2 = '_0To10Percent_'
elif y == '11-30%':
        x_column_subset_value = '11-30%'
        pdf_string2 = '_11To30Percent_'
elif y == '31-50%':
        x_column_subset_value = '31-50%'
        pdf_string2 = '_31To50Percent_'
elif y == '>50%':
        x_column_subset_value = '>50%'
        pdf_string2 = '_GreaterThan50Percent_'
elif y == 'BRIL':
        x_column_subset_value = 'BRIL'
        pdf_string2 = '_BRIL_'
elif y == 'Collaboration Board':
        x_column_subset_value = 'CollaborationBoard'
        pdf_string2 = '_CollaborationBoard_'
elif y == 'Communications':
        x_column_subset_value = 'Communications'
        pdf_string2 = '_Communications_'
elif y == 'DAQ':
        x_column_subset_value = 'DAQ'
        pdf_string2 = '_DAQ_'
elif y == 'ECAL':
        x_column_subset_value = 'ECAL'
        pdf_string2 = '_ECAL_'
elif y == 'Engagement Office':
        x_column_subset_value = 'EngagementOffice'
        pdf_string2 = '_EngagementOffice_'
elif y == 'Extended Executive Board (XEB)':
        x_column_subset_value = 'XEB'
        pdf_string2 = '_XEB_'
elif y == 'HCAL':
        x_column_subset_value = 'HCAL'
        pdf_string2 = '_HCAL_'
elif y == 'HGCAL':
        x_column_subset_value = 'HGCAL'
        pdf_string2 = '_HGCAL_'
elif y == 'L1 Trigger':
        x_column_subset_value = 'L1Trigger'
        pdf_string2 = '_L1Trigger_'
elif y == 'Management Board':
        x_column_subset_value = 'ManagementBoard'
        pdf_string2 = '_ManagementBoard_'
elif y == 'MTD':
        x_column_subset_value = 'MTD'
        pdf_string2 = '_MTD_'
elif y == 'Muon Detector':
        x_column_subset_value = 'MuonDetector'
        pdf_string2 = '_MuonDetector_'
elif y == 'Offline Software and Computing':
        x_column_subset_value = 'OfflineSoftwareAndComputing'
        pdf_string2 = '_OfflineSoftwareAndComputing_'
elif y == 'Physics coordination':
        x_column_subset_value = 'PhysicsCoordination'
        pdf_string2 = '_PhysicsCoordination_'
elif y == 'PPD':
        x_column_subset_value = 'PPD'
        pdf_string2 = '_PPD_'
elif y == 'PPS':
        x_column_subset_value = 'PPS'
        pdf_string2 = '_PPS_'
elif y == 'Regional Representative':
        x_column_subset_value = 'RegionalRepresentative'
        pdf_string2 = '_RegionalRepresentative_'
elif y == 'Run coordination':
        x_column_subset_value = 'RunCoordination'
        pdf_string2 = '_RunCoordination_'
elif y == 'Safety':
        x_column_subset_value = 'Safety'
        pdf_string2 = '_Safety_'
elif y == 'Secretariat':
        x_column_subset_value = 'Secretariat'
        pdf_string2 = 'Secretariat'
elif y == 'Technical coordination':
        x_column_subset_value = 'TechnicalCoordination'
        pdf_string2 = '_TechnicalCoordination_'
elif y == 'Tracker':
        x_column_subset_value = 'Tracker'
        pdf_string2 = 'Tracker'
elif y == 'Trigger coordination':
        x_column_subset_value = 'TriggerCoordination'
        pdf_string2 = '_TriggerCoordination_'
elif y == 'Other':
        x_column_subset_value = 'Other'
        pdf_string2 = '_Other_'
else:
        print('ERROR: Please check the subset requirement.')





#Column with rows in that subset to plot
if z == '9. How often do you read the following webpages? [CERN Document Server (CDS)]':
	webpage_name = ' CDS - '
	x_axis_title = 'Usage frequency'
	pdf_string3 = 'CDS'
	rotation_value = 0
elif z == '9. How often do you read the following webpages? [cms.cern]':
	webpage_name = ' cms.cern - '
	x_axis_title = 'Usage frequency'
	pdf_string3 = 'cms.cern'
	rotation_value = 0
elif z == '9. How often do you read the following webpages? [cmsdoc]':
        webpage_name = ' cmsdoc - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'cms.doc'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [cms-info.web.cern.ch]':
        webpage_name = ' cms-info.web.cern.ch - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'cms-info.web.cern.ch'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [cms-secretariat.web.cern.ch]':
        webpage_name = ' cms-secretariat.web.cern.ch - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'cms-secretariat.web.cern.ch'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [Confluence]':
        webpage_name = ' Confluence - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Confluence'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [How-to docs and similar (https://how-to.docs.cern.ch/)]':
        webpage_name = ' How-to docs and similar are read by - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'HowtoDocsAndSimilar'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [Hypernews - via web]':
        webpage_name = ' Hypernews (via web) - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'HypernewsViaWeb'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [Inspire HEP]':
        webpage_name = ' Inspire HEP - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Inspire_HEP'
        rotation_value = 0
elif z == '9. How often do you read the following webpages? [Twiki pages]':
        webpage_name = ' Twiki pages - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'TwikiPages'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [CERNBOX]':
        webpage_name = ' CERNBox - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CERNBox'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [CINCO]':
        webpage_name = ' CINCO - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CINCO'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [cmscentre]':
        webpage_name = '  cmscentre - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'cmscentre'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [cmsonline]':
        webpage_name = ' cmsonline - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'cmsonline'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [cms-talk.web.cern.ch]':
        webpage_name = ' cms-talk - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'cmstalk'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Collabora]':
        webpage_name = ' Collabora - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'collabora'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [CodiMD]':
        webpage_name = ' CodiMD - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CodiMD'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [DocDB]':
        webpage_name = ' DocDB - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'DocDB'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Drawio]':
        webpage_name = ' Drawio - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Drawio'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [e-groups]':
        webpage_name = ' e-groups are used by'
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'egroups'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [e-log]':
        webpage_name = ' e-log - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'elog'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Email]':
        webpage_name = ' email - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'email'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Foswiki]':
        webpage_name = ' Foswiki - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Foswiki'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Gantt viewer]':
        webpage_name = ' Gantt viewer - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'GanttViewer'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [GitHub]':
        webpage_name = ' GitHub - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'GitHub'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Gitlab]':
        webpage_name = ' Gitlab - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Gitlab'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [GoogleDocs]':
        webpage_name = ' GoogleDocs are used by - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'GoogleDocs'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Hypernews via the web, not mail]':
        webpage_name = ' Hypernews via the web (not mail) - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'HypernewsViaWebNotMail'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [iCMS]':
        webpage_name = ' iCMS  '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'iCMS'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Indico]':
        webpage_name = ' Indico - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = ' Indico'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [JIRA]':
        webpage_name = ' JIRA - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'JIRA'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [MS Office]':
        webpage_name = ' MS Office - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'MSOffice'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [OnlyOffice]':
        webpage_name = ' OnlyOffice - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'OnlyOffice'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Overleaf]':
        webpage_name = ' Overleaf - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Overleaf'
        rotation_value = 0
elif z == '10. How often do you use the following tools? [Zenodo/Invenio]':
        webpage_name = ' Zenodo/Invenio - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Zenodo'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Discord]':
        webpage_name = '  Discord - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Discord'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Facebook messenger]':
        webpage_name = ' Facebook messenger - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'FacebookMessenger'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Mattermost]':
        webpage_name = '  Mattermost - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Mattermost'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Skype]':
        webpage_name = ' Skype  '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Skype'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Signal]':
        webpage_name = ' Signal - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Signal'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Slack]':
        webpage_name = ' Slack - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Slack'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Whatsapp]':
        webpage_name = ' Whatsapp  '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Whatsapp'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zoom]':
        webpage_name = ' Zoom - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Zoom'
        rotation_value = 0
elif z == '11. How often do you use the following platforms for communicating with other members of the collaboration? [Zulip]':
        webpage_name = ' Zulip - '
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'Zulip'
        rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Facebook page (https://www.facebook.com/CMSexperiment/)]":
	webpage_name = " CMS experiment's Facebook page - "
	x_axis_title = 'Usage frequency'
	pdf_string3 = 'CMS_Fb'
	rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Twitter account (https://twitter.com/CMSExperiment)]":
        webpage_name = " CMS experiment's Twitter account  "
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMS_Twitter'
        rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS experiment's Instagram account (https://www.instagram.com/cmsexperiment)]":
        webpage_name = " CMS experiment's Instagram account - "
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMS_Instagram'
        rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS experiment's YouTube Channel (https://www.youtube.com/user/CMSExperimentTV )]":
        webpage_name = " CMS experiment's YouTube Channel - "
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMS_YouTube'
        rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS Muon Group's Twitter account (https://twitter.com/CmsMuon)]":
        webpage_name = " CMS Muon Group's Twitter account - "
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMS_Muon_Twitter'
        rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS Publications Twitter account (https://twitter.com/CMSpapers)]":
        webpage_name = " CMS Publications Twitter account - "
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMS_Publications_Twitter'
        rotation_value = 0
elif z == "12. How often do you read posts on the following social media accounts?  [CMS Young Scientist Committee's Facebook group (https://www.facebook.com/groups/843805749716562)]":
        webpage_name = " CMS Young Scientist Committee's Facebook group - "
        x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMS_YSC_Fb'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS awards]":
	webpage_name = " CMS awards - "
        x_axis_title = 'Platform'
        pdf_string3 = 'CMS_Awards'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [CMS public briefings]":
	webpage_name = " CMS public briefings - "
        x_axis_title = 'Platform'
        pdf_string3 = 'CMS_PublicBriefings'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Conferences]":
	webpage_name = " Conferences - "
        x_axis_title = 'Platform'
        pdf_string3 = 'Conferences'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [General announcements]":
	webpage_name = " General announcements - "
        x_axis_title = 'Platform'
        pdf_string3 = 'GeneralAnnouncements'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Jobs]":
	webpage_name = " Jobs - "
        x_axis_title = 'Platform'
        pdf_string3 = 'Jobs'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Meetings]":
	webpage_name = " Meetings - "
        x_axis_title = 'Platform'
        pdf_string3 = 'Meetings'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Nominations]":
	webpage_name = " Nominations - "
        x_axis_title = 'Platform'
        pdf_string3 = 'Nominations'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Safety alerts]":
	webpage_name = " Safety alerts - "
        x_axis_title = 'Platform'
        pdf_string3 = 'SafetyAlerts'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Security alerts]":
	webpage_name = " Safety alerts - "
        x_axis_title = 'Platform'
        pdf_string3 = 'SafetyAlerts'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Social events]":
	webpage_name = " Social events - "
        x_axis_title = 'Platform'
        pdf_string3 = 'SocialEvents'
        rotation_value = 0
elif z == "13. Which platform(s) is/are your main source(s) for receiving information about the following collaboration announcements?  Please scroll to the right to see all options. [Publications]":
	webpage_name = " Publications - "
        x_axis_title = 'Platform'
        pdf_string3 = 'Publications'
        rotation_value = 5
elif z == "15. In the past two years, how often do you attended/read/watched the following? [CMS Week Monday plenary ]":
	webpage_name = " CMS Week Monday plenary - "
	x_axis_title = 'Usage frequency'
        pdf_string3 = 'CMSWeek_MondayPlenary'
        rotation_value = 0
elif z == "15. In the past two years, how often do you attended/read/watched the following? [Other CMS Week sessions]":
	webpage_name = " Other CMS Week sessions - "
	x_axis_title = 'Usage frequency'
        pdf_string3 = 'OtherCMSWeekSessions'
        rotation_value = 0
elif z == "15. In the past two years, how often do you attended/read/watched the following? [Weekly General Meeting]":
	webpage_name = " WGM - "
	x_axis_title = 'Usage frequency'
        pdf_string3 = 'WGM'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Discord]":
	webpage_name = " Discord - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfDiscord'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Facebook messenger]":
	webpage_name = " Facebook messenger - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfFbMessenger'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Mattermost]":
	webpage_name = " Mattermost - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfMattermost'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Skype]":
	webpage_name = " Skype - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfSkype'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Signal]":
	webpage_name = " Signal - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfSignal'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Slack]":
	webpage_name = " Slack - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfSlack'
        rotation_value = 0
elif z == "16. Please indicate your favourite three messaging applications for messaging other members of the CMS collaboration (1 = preferred application). [Whatsapp]":
	webpage_name = " Whatsapp - "
        x_axis_title = 'Rank'
        pdf_string3 = 'PreferenceOfWhatsapp'
        rotation_value = 0
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accesibility of information]":
	webpage_name = " Accessibility of information - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'AccessibilityOfInformation'
        rotation_value = 10
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Accuracy of content]":
	webpage_name = " Accuracy of content - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'AccuracyOfContent'
        rotation_value = 10
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Amount of information]": 
	webpage_name = " Amount of information - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'AmountOfInformation'
        rotation_value = 10 
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Clarity of information]":
	webpage_name = " Clarity of information - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'ClarityOfInformation'
        rotation_value = 10 
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of delivery of information]":  
	webpage_name = " Frequency of delivery of information - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'FrequencyOfDeliveryOfInformation'
        rotation_value = 10 
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Frequency of receipt of information]":   
	webpage_name = " Frequency of receipt of information - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'FrequencyOfReceiptOfInformation'
        rotation_value = 10 
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Relevance of material]":
	webpage_name = " Relevance of material - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'RelevanceOfMaterial'
        rotation_value = 10 
elif z == "18. In general, how satisfied are you with the following aspects of CMS internal communication as a whole? [Style of presentation]":
	webpage_name = " Style of presentation - "
        x_axis_title = 'Satisfaction'
        pdf_string3 = 'StyleOfPresentation'
        rotation_value = 10
else:
	print('ERROR: Please check the chosen column name for the column you would like to plot.')

#Subsetting the data and counting the number of responses 
Column_Subset = df[df[x].str.contains(y)]
Plotted_Column = Column_Subset[z].value_counts()

#Plotting
Plotted_Column.plot.bar()
plt.title(webpage_name + x_column_subset + x_column_subset_value)
plt.xlabel(x_axis_title)
plt.xticks(rotation = rotation_value)
plt.ylabel("Number of responses")
plt.savefig(pdf_string1 + pdf_string2 + pdf_string3 + '.pdf')

