from flask import Flask, render_template, request

app = Flask(__name__)


def get_response(user_input):
    user_input = user_input.lower()
    
    if "tko je andrija mohorovičić" in user_input or "andrija mohorovičić" in user_input:
        return "To sam ja! Bio sam hrvatski seizmolog, najpoznatiji po otkriću Mohorovičićeve diskontinuiteta. "
    
    elif "tko si ti?" in user_input or "tko" in user_input:
        return "Ja sam Andrija Mohorovičić. Bio sam hrvatski seizmolog, a moje najpoznatije otkriće je Mohorovičićev diskontinuitet"
    
    elif "kako si otkrio diskontinuitet kojeg sada nazivamo mohorovičićev diskontinuitet" in user_input or "mohorovičićev diskontinuitet" in user_input:
        return "Otkrio sam diskontinuitet u Zemljinoj unutrašnjosti 1909. godine, analizirajući podatke o seizmičkim valovima koji putuju kroz Zemlju. Kroz proučavanje brzina seizmičkih valova shvatio sam da se brzina P-valova naglo mijenja na određenoj dubini, što mi je ukazalo na postojanje sloja unutar Zemlje u kojem dolazi do drastične promjene u gustoći i sastavu materijala. Ovaj sloj, danas poznat kao Mohorovičićev diskontinuitet, označava prijelaz između Zemljine kore i plašta. To je bilo jedno od najvažnijih otkrića u geofizici jer je omogućilo bolje razumijevanje strukture Zemlje."

    elif "što misliš o gimnaziji andrije mohorovičića" in user_input or "što misliš o GAM-u" in user_input or "što misliš o našoj školi?" in user_input:
        return "Ponosan sam što postoji škola nazvana po meni i vjerujem da obrazovanje vodi napretku."
    
    elif "koji su poznati suvremenici u tvoje doba" in user_input or "poznati suvremenici" in user_input or "koga si sve upoznao?" in user_input:
        return "U Pragu sam mogao upoznati Gregora Mendela, Alfreda Nobela, Maxa Plancka i R.M. Rilkea. U Rijeci sam upoznao Ivanu Brlić-Mažuranić, Vladimira Nazora, Franju Račkog i Janka Polića Kamova. U Zagrebu, Vladimira Preloga i Stjepana Radića."
    
    elif "koje su druge znamenite osobe" in user_input:
        return "Među mojim utjecajima su Augustin Jean Fresnel, Hermann von Helmholtz, Ivan Vukić, Zagrebačko sveučilište i JAZU."
    
    elif "nefoskop" in user_input or "što je nefoskop?" in user_input:
        return "Nefoskop je bio moj izum, alat koji sam razvio kako bih proučavao brzinu seizmičkih valova kroz Zemlju. Kasnije mi je pomoglo sa istraživanjem unutrašnje strukture Zemlje."
    
    elif "koje si mediteranske pojave proučavao" in user_input:
        return "Proučavao sam potrese u Rijeci, Istri i ostatku Kvarnera, koji su imali veliki utjecaj na moju karijeru."
    
    elif "privržen otac i suprug" in user_input:
        return "Da, bio sam vrlo privržen otac i suprug. Smrt mog sina 1912. godine jako me pogodila, pa sam provodio više vremena sa suprugom Silvijom."
    
    elif "kakav si otac"  in user_input or "što je tvoj sin rekao o tebi?"  in user_input:
        return "Moj sin Stjepan je o meni rekao: 'Bio je vedar i dobroćudan čovjek, čiji je život bio pod strogim redom, kao i njegov kronometar.'"
    
    elif "intelektualac" in user_input or "čujem da su te prozvali intelektualcem, kako to?" in user_input:
        return "Zanimale su me stvari izvan moje specijalizacije. Čitao sam strane novine, govorio nekoliko jezika, i bio sam vrlo upućen u aktualnosti hrvatske politike."
    
    elif "duhan" in user_input:
        return "Moj najveći porok bio je duhan, kojeg nikad nisam prestao pušiti."
    
    elif "smrt" in user_input or "kada si umro" or "18. prosinca 1936." in user_input:
        return "Moj se život okončao 18. prosinca 1936. godine, a taj dan bio je petak, kao što sam uvijek govorio da se važne stvari događaju petkom."
    
    elif "knjizevnici suvremenici" in user_input:
        return "U Pragu i Trstu su živjeli poznati književnici poput R.M. Rilkea i drugih intelektualaca."
    
    elif "rijeka" in user_input:
        return "Priroda u Trstu i Rijeci me fascinirala, posebno vjetrovi koji su ostavili snažan utjecaj na moj rad."
    
    elif "kada ste rođeni" in user_input or "kada je rođen andrija mohorovičić" in user_input:
        return "Rođen sam 23. siječnja 1857. godine."

    elif "gdje ste rođeni" in user_input or "gdje je rođen andrija mohorovičić" in user_input:
        return "Rođen sam u Voloskom, malom naselju blizu Opatije, na jadranskoj obali."

    elif "tko su bili vaši roditelji" in user_input or "tko su bili roditelji andrije mohorovičića" in user_input:
        return "Moj otac bio je kapetan pomorske flote, a majka je bila domaćica. Obitelj je bila skromna, ali poticala nas je na obrazovanje."

    elif "imate li braće i sestara" in user_input or "je li andrija mohorovičić imao braću" in user_input:
        return "Imao sam nekoliko braće i sestara, iako sam bio najmlađi u obitelji."

    elif "imali ste djece" in user_input or "je li andrija mohorovičić imao djece" in user_input:
        return "Da, imao sam sina, koji je nastavio moj obiteljski naslijeđeni interes za znanost."

    elif "koji su bili vaši obrazovni počeci" in user_input or "gdje je andrija mohorovičić studirao" in user_input:
        return "Školovao sam se u Rijeci, a kasnije sam studirao na Sveučilištu u Zagrebu, gdje sam se posvetio studiju prirodnih znanosti."

    elif "kako je obitelj reagirala na vaš izbor karijere" in user_input or "kako su roditelji reagirali na znanstvenu karijeru" in user_input:
        return "Moji roditelji su uvijek podržavali moju želju za znanjem, iako nisu bili znanstvenici. Moj otac, kao pomorski časnik, razumio je važnost istraživanja i znanja o Zemlji."
    
    else:
        return "Nažalost, u moje doba nismo se služili ovakvim rječnikom. Pokušaj ponovno!"

@app.route('/', methods=['GET', 'POST'])
def home():
    response = ''
    if request.method == 'POST':
        user_input = request.form['user_input']
        print(user_input)
        response = get_response(user_input)
        print(response)
    return render_template('index.html', response=response)

