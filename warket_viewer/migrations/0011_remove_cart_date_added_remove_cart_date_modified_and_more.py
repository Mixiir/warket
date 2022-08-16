# Generated by Django 4.1 on 2022-08-16 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('warket_viewer', '0010_delete_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='date_modified',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_amount',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_currency',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_details',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_method',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='total',
        ),
        migrations.RemoveField(
            model_name='wine',
            name='price',
        ),
        migrations.AlterField(
            model_name='cart',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='cart',
            name='status',
            field=models.CharField(default='cart', max_length=100),
        ),
        migrations.AlterField(
            model_name='wine',
            name='price_per_unit',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wine',
            name='rating',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='type',
            field=models.CharField(choices=[('Red', 'Red'), ('White', 'White'), ('Sparkling', 'Sparkling'), ('Rose', 'Rose'), ('Dessert', 'Dessert'), ('Other', 'Other')], default='red', max_length=100),
        ),
        migrations.AlterField(
            model_name='wine',
            name='units_in_auction',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='wine',
            name='units_in_stock',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='wine',
            name='variety',
            field=models.CharField(choices=[('Abbuoto', 'Abbuoto'), ('Abouriou', 'Abouriou'), ('Abrusco', 'Abrusco'), ('Acitana', 'Acitana'), ('Acolon', 'Acolon'), ('Ada Karasi', 'Ada Karasi'), ('Affenthaler', 'Affenthaler'), ('Agiorgitiko', 'Agiorgitiko'), ('Aglianico', 'Aglianico'), ('Aglianicone', 'Aglianicone'), ('Agni (grape) [cs]', 'Agni (grape) [cs]'), ('Agronomica', 'Agronomica'), ('Agua Santa', 'Agua Santa'), ('Aidani Mavro', 'Aidani Mavro'), ('Aladasturi', 'Aladasturi'), ('Albaranzeuli nero', 'Albaranzeuli nero'), ('Albarossa', 'Albarossa'), ('Aleatico', 'Aleatico'), ('Aleksandrouli', 'Aleksandrouli'), ('Alexander', 'Alexander'), ('Alfrocheiro', 'Alfrocheiro'), ('Alicante Henri Bouschet', 'Alicante Henri Bouschet'), ('Allegro', 'Allegro'), ('Amaral', 'Amaral'), ('Ancellotta', 'Ancellotta'), ('André (grape) [cs]', 'André (grape) [cs]'), ('Antey Magarachsky', 'Antey Magarachsky'), ('Aramon Noir', 'Aramon Noir'), ('Areni', 'Areni'), ('Argaman', 'Argaman'), ('Argant', 'Argant'), ('Arinarnoa', 'Arinarnoa'), ('Arinto de Bucelas', 'Arinto de Bucelas'), ('Arnsburger', 'Arnsburger'), ('Arrouya', 'Arrouya'), ('Ashughaji', 'Ashughaji'), ('Aspiran Bouschet', 'Aspiran Bouschet'), ('Aspiran Noir', 'Aspiran Noir'), ('Assario', 'Assario'), ('Asuretuli Shavi', 'Asuretuli Shavi'), ('Aubun', 'Aubun'), ('Avanà', 'Avanà'), ('Avarengo', 'Avarengo'), ('Avgoustiatis', 'Avgoustiatis'), ('Băbească neagră', 'Băbească neagră'), ('Babić', 'Babić'), ('Bachet Noir', 'Bachet Noir'), ('Baco Noir', 'Baco Noir'), ('Baga', 'Baga'), ('Barbera', 'Barbera'), ('Barbera del Sannio', 'Barbera del Sannio'), ('Barbera Sarda', 'Barbera Sarda'), ('Barsaglina', 'Barsaglina'), ('Bastardo Magarachsky', 'Bastardo Magarachsky'), ('Beaunoir', 'Beaunoir'), ('Béclan', 'Béclan'), ('Beichun', 'Beichun'), ('Bekari', 'Bekari'), ('Belat', 'Belat'), ('Béquignol Noir', 'Béquignol Noir'), ('Biborkadarka', 'Biborkadarka'), ('Black Queen', 'Black Queen'), ('Blatina', 'Blatina'), ('Blauburger', 'Blauburger'), ('Blauer Arbst / Pinot Noir', 'Blauer Arbst / Pinot Noir'), ('Blauer Wildbacher', 'Blauer Wildbacher'), ('Blaufränkisch / Limberger', 'Blaufränkisch / Limberger'), ('Bobal', 'Bobal'), ('Boğazkere', 'Boğazkere'), ('Bombino Nero', 'Bombino Nero'), ('Bonamico', 'Bonamico'), ('Bonarda Piemontese', 'Bonarda Piemontese'), ('Bonda', 'Bonda'), ('Bondola', 'Bondola'), ('Bondoletta', 'Bondoletta'), ('Bonvedro', 'Bonvedro'), ('Borba', 'Borba'), ('Borracal', 'Borracal'), ('Bouchalès', 'Bouchalès'), ('Bourrisquou', 'Bourrisquou'), ('Bouteillan Noir', 'Bouteillan Noir'), ('Bovale Grande', 'Bovale Grande'), ('Bovale Sardo', 'Bovale Sardo'), ('Bracciola Nera', 'Bracciola Nera'), ('Brachetto del Piemonte', 'Brachetto del Piemonte'), ('Brancellao', 'Brancellao'), ('Braquet Noir', 'Braquet Noir'), ('Brugnola', 'Brugnola'), ('Brujidera', 'Brujidera'), ('Brun Argenté', 'Brun Argenté'), ('Brun Fourca', 'Brun Fourca'), ('Brunal', 'Brunal'), ('Brunello', 'Brunello'), ('Bubbierasco', 'Bubbierasco'), ('Buket', 'Buket'), ('Busuioaca de Bohotin', 'Busuioaca de Bohotin'), ('Caberinta', 'Caberinta'), ('Cabernet Carbon', 'Cabernet Carbon'), ('Cabernet Carol', 'Cabernet Carol'), ('Cabernet Colonjes', 'Cabernet Colonjes'), ('Cabernet Cortis', 'Cabernet Cortis'), ('Cabernet Cubin', 'Cabernet Cubin'), ('Cabernet Dorio', 'Cabernet Dorio'), ('Cabernet Dorsa', 'Cabernet Dorsa'), ('Cabernet Franc', 'Cabernet Franc'), ('Cabernet Gernischt', 'Cabernet Gernischt'), ('Cabernet Jura', 'Cabernet Jura'), ('Cabernet Mitos', 'Cabernet Mitos'), ('Cabernet Moravia', 'Cabernet Moravia'), ('Cabernet Pfeffer', 'Cabernet Pfeffer'), ('Cabernet Sauvignon', 'Cabernet Sauvignon'), ('Cabernet Severny', 'Cabernet Severny'), ('Cabertin', 'Cabertin'), ('Caddiu', 'Caddiu'), ('Cagnulari', 'Cagnulari'), ('Caino Bravo', 'Caino Bravo'), ('Caiño Tinto', 'Caiño Tinto'), ('Calabrese', 'Calabrese'), ('Calabrese di Montenuovo', 'Calabrese di Montenuovo'), ('Caladoc', 'Caladoc'), ('Calandro', 'Calandro'), ('Calitor Noir', 'Calitor Noir'), ('Çalkarası', 'Çalkarası'), ('Callet', 'Callet'), ('Caloria', 'Caloria'), ('Camaraou Noir', 'Camaraou Noir'), ('Camarate', 'Camarate'), ('Camarese', 'Camarese'), ('Campbell Early', 'Campbell Early'), ('Canaiolo Nero', 'Canaiolo Nero'), ('Canari Noir', 'Canari Noir'), ('Canina Nera', 'Canina Nera'), ('Cannamela', 'Cannamela'), ('Carcajolo Nero', 'Carcajolo Nero'), ('Caricagiola', 'Caricagiola'), ('Carignan', 'Carignan'), ('Carinena', 'Carinena'), ('Carménère', 'Carménère'), ('Carmine', 'Carmine'), ('Carminoir', 'Carminoir'), ('Carnelian', 'Carnelian'), ('Carrasquin', 'Carrasquin'), ('Carricante', 'Carricante'), ('Casavecchia', 'Casavecchia'), ('Cascade', 'Cascade'), ('Casculho', 'Casculho'), ('Casetta', 'Casetta'), ('Castagnara', 'Castagnara'), ('Castelão', 'Castelão'), ('Castets', 'Castets'), ('Castiglione', 'Castiglione'), ('Catalanesca', 'Catalanesca'), ('Catanese Nero', 'Catanese Nero'), ('Cavrara', 'Cavrara'), ('Centesimino', 'Centesimino'), ('Centurian', 'Centurian'), ('Cereza', 'Cereza'), ('Cesanese', 'Cesanese'), ('César', 'César'), ('Cevat Kara', 'Cevat Kara'), ('Chambourcin', 'Chambourcin'), ('Charbono', 'Charbono'), ('Chancellor', 'Chancellor'), ('Charentsi', 'Charentsi'), ('Chatus', 'Chatus'), ('Chelois', 'Chelois'), ('Chenanson', 'Chenanson'), ('Chichaud', 'Chichaud'), ('Chidiriotiko', 'Chidiriotiko'), ('Chisago', 'Chisago'), ('Chkhaveri', 'Chkhaveri'), ('Chondromavro', 'Chondromavro'), ('Cianorie', 'Cianorie'), ('Cienna', 'Cienna'), ('Ciliegiolo', 'Ciliegiolo'), ('Cinsaut', 'Cinsaut'), ('Colombana nera', 'Colombana nera'), ('Colorino', 'Colorino'), ('Complexa', 'Complexa'), ('Cornalin see Rouge du Pays', 'Cornalin see Rouge du Pays'), ('Cornifesto', 'Cornifesto'), ('Corvina / Corvinone', 'Corvina / Corvinone'), ('Counoise', 'Counoise'), ('Croatina', 'Croatina'), ('Darnekuša', 'Darnekuša'), ('Dobričić', 'Dobričić'), ('Dolcetto', 'Dolcetto'), ('Domina', 'Domina'), ('Dornfelder', 'Dornfelder'), ('Douce noir', 'Douce noir'), ('Douce Noire grise', 'Douce Noire grise'), ('Dunkelfelder', 'Dunkelfelder'), ('Duras', 'Duras'), ('Dureza', 'Dureza'), ('Durif / Petite Sirah', 'Durif / Petite Sirah'), ('Ederena', 'Ederena'), ('Enfariné noir', 'Enfariné noir'), ('Espadeiro', 'Espadeiro'), ('Étraire', 'Étraire'), ('Fer', 'Fer'), ('Ferrón', 'Ferrón'), ('Fetească neagră', 'Fetească neagră'), ('Forcallat tinta', 'Forcallat tinta'), ('Fortana', 'Fortana'), ('Frappato', 'Frappato'), ('Freisa', 'Freisa'), ('Frühroter Veltliner', 'Frühroter Veltliner'), ('Fumin', 'Fumin'), ('Gaglioppo', 'Gaglioppo'), ('Gamashara', 'Gamashara'), ('Gamay / Gamay noir', 'Gamay / Gamay noir'), ('Gamaret', 'Gamaret'), ('Garanoir', 'Garanoir'), ('Garnatxa / Grenache / Garnacha / Cannonau /Lladoner Pelut / Lledoner Pelut', 'Garnatxa / Grenache / Garnacha / Cannonau /Lladoner Pelut / Lledoner Pelut'), ('Garró', 'Garró'), ('Ġellewża', 'Ġellewża'), ('Girò', 'Girò'), ('Gouget noir', 'Gouget noir'), ('Graciano', 'Graciano'), ('Grand noir de la Calmette', 'Grand noir de la Calmette'), ('Grisa nera', 'Grisa nera'), ('Greco nero', 'Greco nero'), ('Grignolino', 'Grignolino'), ('Gropello', 'Gropello'), ('Grolleau / Groslot', 'Grolleau / Groslot'), ('Gros Verdot', 'Gros Verdot'), ('Gueuche noir', 'Gueuche noir'), ('Helfensteiner', 'Helfensteiner'), ('Heroldrebe', 'Heroldrebe'), ('Hondarribi Beltza', 'Hondarribi Beltza'), ('Hron', 'Hron'), ("Humagne Rouge / Cornalin d'Aoste", "Humagne Rouge / Cornalin d'Aoste"), ('Joubertin / Jaubertin', 'Joubertin / Jaubertin'), ('Juan García', 'Juan García'), ('Jurancon noir', 'Jurancon noir'), ('Kadarka', 'Kadarka'), ('Kakhet', 'Kakhet'), ('Kalecik Karasi', 'Kalecik Karasi'), ('Kindzmarauli/ Saperavi', 'Kindzmarauli/ Saperavi'), ('Kotsifali', 'Kotsifali'), ('Krasnostop Zolotovsky', 'Krasnostop Zolotovsky'), ('Kratosija', 'Kratosija'), ('Lacrima di Morro / Lacrima nera', 'Lacrima di Morro / Lacrima nera'), ('Lagrein', 'Lagrein'), ('Lambrusco', 'Lambrusco'), ('Liatiko', 'Liatiko'), ('Limnio', 'Limnio'), ('Listan negro', 'Listan negro'), ('Loureira Tinta', 'Loureira Tinta'), ('Madrasa/ Matrassa', 'Madrasa/ Matrassa'), ('Magarach Bastardo/Bastardo Magarach', 'Magarach Bastardo/Bastardo Magarach'), ('Magaratch Ruby / Magarach Ruby', 'Magaratch Ruby / Magarach Ruby'), ('Magliocco Canino/Maiolica', 'Magliocco Canino/Maiolica'), ('Magliocco Dolce/Marsigliana nera', 'Magliocco Dolce/Marsigliana nera'), ('Magyarfrankos', 'Magyarfrankos'), ('Malbec', 'Malbec'), ('Malvasia di Schierano/Malvasia nera', 'Malvasia di Schierano/Malvasia nera'), ('Mammolo', 'Mammolo'), ('Mandelaria / Mandelari / Amorghiano', 'Mandelaria / Mandelari / Amorghiano'), ('Mandolari', 'Mandolari'), ('Manseng noir', 'Manseng noir'), ('Manto negro', 'Manto negro'), ('Mara', 'Mara'), ('Maratheftiko', 'Maratheftiko'), ('Marselan', 'Marselan'), ('Marsigliana', 'Marsigliana'), ('Marzemino', 'Marzemino'), ('Mauzac noir', 'Mauzac noir'), ('Mavro', 'Mavro'), ('Mavrodafni / Mavrodaphne', 'Mavrodafni / Mavrodaphne'), ('Mavrud / Mavroudi', 'Mavrud / Mavroudi'), ('Mayorquin', 'Mayorquin'), ('Meghrabujr', 'Meghrabujr'), ('Melnik', 'Melnik'), ('Mencía / Jaén colorado', 'Mencía / Jaén colorado'), ('Merenzao', 'Merenzao'), ('Merille', 'Merille'), ('Merlot', 'Merlot'), ('Milgranet', 'Milgranet'), ('Millot /Léon Millot', 'Millot /Léon Millot'), ('Mission', 'Mission'), ('Molinara', 'Molinara'), ('Mondeuse', 'Mondeuse'), ('Monica', 'Monica'), ('Montepulciano', 'Montepulciano'), ('Montù / Montuni', 'Montù / Montuni'), ('Moreto', 'Moreto'), ('Moristel', 'Moristel'), ('Mornen noir', 'Mornen noir'), ('Morrastel Bouschet', 'Morrastel Bouschet'), ('Mourisco tinto', 'Mourisco tinto'), ('Mourvèdre / Monastrell / Mataro/ Rossola nera/Garrut', 'Mourvèdre / Monastrell / Mataro/ Rossola nera/Garrut'), ('Mouyssaguès', 'Mouyssaguès'), ('Mtevandidi', 'Mtevandidi'), ('Mujuretuli', 'Mujuretuli'), ('Muscardin', 'Muscardin'), ('Muscat Bouschet', 'Muscat Bouschet'), ('Muscat Hamburg', 'Muscat Hamburg'), ('Nebbiolo', 'Nebbiolo'), ('Negoska', 'Negoska'), ('Negrara', 'Negrara'), ('Négrette/ Pinot St. George', 'Négrette/ Pinot St. George'), ('Negroamaro', 'Negroamaro'), ('Negru de Dragasani', 'Negru de Dragasani'), ('Nerkarat', 'Nerkarat'), ('Nero Buono di Cori', 'Nero Buono di Cori'), ("Nero d'Avola", "Nero d'Avola"), ('Nerello Mascalese', 'Nerello Mascalese'), ('Nerello Cappuccio', 'Nerello Cappuccio'), ('Neretto di Bairo', 'Neretto di Bairo'), ('Neyret', 'Neyret'), ('Nielluccio', 'Nielluccio'), ('Ninčuša', 'Ninčuša'), ('Nocera', 'Nocera'), ('Notardomenico', 'Notardomenico'), ('Oeillade noire', 'Oeillade noire'), ('Ojaleshi', 'Ojaleshi'), ('Öküzgözü', 'Öküzgözü'), ('Oseleta', 'Oseleta'), ('Pais', 'Pais'), ('Pallagrello nero', 'Pallagrello nero'), ('Pamid', 'Pamid'), ('Pascale di Cagliari', 'Pascale di Cagliari'), ('Pelaverga', 'Pelaverga'), ('Peloursin', 'Peloursin'), ('Perdal', 'Perdal'), ('Perricone/Guarnaccia', 'Perricone/Guarnaccia'), ('Persan', 'Persan'), ('Petit Bouschet', 'Petit Bouschet'), ('Petit Rouge', 'Petit Rouge'), ('Petit Verdot', 'Petit Verdot'), ('Piccola nera', 'Piccola nera'), ('Piedirosso', 'Piedirosso'), ('Pignerol', 'Pignerol'), ('Pignola Valtellinese', 'Pignola Valtellinese'), ('Pignolo', 'Pignolo'), ("Pineau d'Aunis", "Pineau d'Aunis"), ('Pinot Meunier / Schwarzriesling / Müllerebe', 'Pinot Meunier / Schwarzriesling / Müllerebe'), ('Pinot Noir / Spätburgunder / Blauburgunder / Pinot Nero', 'Pinot Noir / Spätburgunder / Blauburgunder / Pinot Nero'), ('Pinotage', 'Pinotage'), ('Piquepoul noir', 'Piquepoul noir'), ('Plassa', 'Plassa'), ('Plavina', 'Plavina'), ('Pollera nera', 'Pollera nera'), ('Portan', 'Portan'), ('Poulsard/ Plousard', 'Poulsard/ Plousard'), ('Prieto Picudo', 'Prieto Picudo'), ('Prokupac', 'Prokupac'), ('Raboso', 'Raboso'), ('Ramisco', 'Ramisco'), ('Reberger', 'Reberger'), ('Refosco / Refošk', 'Refosco / Refošk'), ('Rimava', 'Rimava'), ('Roesler', 'Roesler'), ('Rondinella', 'Rondinella'), ('Rossese', 'Rossese'), ('Rossignola', 'Rossignola'), ('Rossolino nero', 'Rossolino nero'), ('Rotberger', 'Rotberger'), ('Rouchet/ Ruché / Roche', 'Rouchet/ Ruché / Roche'), ('Rubintos', 'Rubintos'), ('Ruby Cabernet', 'Ruby Cabernet'), ('Rufete / Tinta Pinheira / Tinta Carvalha / Rufeta', 'Rufete / Tinta Pinheira / Tinta Carvalha / Rufeta'), ('Sagrantino', 'Sagrantino'), ('Sangiovese', 'Sangiovese'), ('San Giuseppe nero', 'San Giuseppe nero'), ('Saperavi', 'Saperavi'), ('Schiava / Trollinger / Vernatsch', 'Schiava / Trollinger / Vernatsch'), ('Schioppettino', 'Schioppettino'), ('Schönburger', 'Schönburger'), ('Sciacarello', 'Sciacarello'), ('Sciascinoso / Olivella nera', 'Sciascinoso / Olivella nera'), ('Segalin / Ségalin', 'Segalin / Ségalin'), ('Servanin', 'Servanin'), ('Sgaretta/Sgavetta', 'Sgaretta/Sgavetta'), ('Shiraz / Syrah', 'Shiraz / Syrah'), ('Shiroka Melnishka Losa / Melnik', 'Shiroka Melnishka Losa / Melnik'), ('Sousão/Souzão/Sousón', 'Sousão/Souzão/Sousón'), ('St. Laurent / Svatovavrinecke', 'St. Laurent / Svatovavrinecke'), ('Saint-Macaire', 'Saint-Macaire'), ('Sumoll', 'Sumoll'), ('Susumaniello', 'Susumaniello'), ('Tannat', 'Tannat'), ('Tarrango', 'Tarrango'), ('Tazzelenghe', 'Tazzelenghe'), ('Tempranillo / Aragónez / Tinta Roriz / Ull de Llebre / Cencibel / Tinta del Pais', 'Tempranillo / Aragónez / Tinta Roriz / Ull de Llebre / Cencibel / Tinta del Pais'), ('Teran', 'Teran'), ('Termarina rossa', 'Termarina rossa'), ('Teroldego / Teroldego Rotaliano', 'Teroldego / Teroldego Rotaliano'), ('Terret noir', 'Terret noir'), ('Thiniatiko', 'Thiniatiko'), ('Tibouren', 'Tibouren'), ('Tinta Amarela', 'Tinta Amarela'), ('Tinta Barroca', 'Tinta Barroca'), ('Tinta Caiada', 'Tinta Caiada'), ('Tinta Carvalha', 'Tinta Carvalha'), ('Tinta Francisca', 'Tinta Francisca'), ('Tinta Madeira', 'Tinta Madeira'), ('Tinta Miuda', 'Tinta Miuda'), ('Tinta Negra Mole / Preto Martinho', 'Tinta Negra Mole / Preto Martinho'), ('Tinto Cão', 'Tinto Cão'), ('Touriga Franca / Touriga Francesa', 'Touriga Franca / Touriga Francesa'), ('Touriga Nacional / Azal Espanhol / Preto de Mortágua', 'Touriga Nacional / Azal Espanhol / Preto de Mortágua'), ('Turán', 'Turán'), ('Trepat', 'Trepat'), ('Trevisana nera', 'Trevisana nera'), ('Trincadeira/ Castelão / Torneiro', 'Trincadeira/ Castelão / Torneiro'), ('Usakhelauri', 'Usakhelauri'), ('Uva di Troia', 'Uva di Troia'), ('Uvalino', 'Uvalino'), ('Uva Rara', 'Uva Rara'), ('Uva Tosca', 'Uva Tosca'), ('Vaccarese / Vaccarèse/ Brun Argenté', 'Vaccarese / Vaccarèse/ Brun Argenté'), ('Valdiguié / Brocol / Napa Gamay / Gamay 15', 'Valdiguié / Brocol / Napa Gamay / Gamay 15'), ('Valentino nero', 'Valentino nero'), ('Vermentino nero', 'Vermentino nero'), ('Vespolina', 'Vespolina'), ('Vien de Nus', 'Vien de Nus'), ('Volidza/Volitsa', 'Volidza/Volitsa'), ('Vranac', 'Vranac'), ('Vuillermin', 'Vuillermin'), ('Wildbacher/Blauer Wildbacher', 'Wildbacher/Blauer Wildbacher'), ('Wrothham Pinot', 'Wrothham Pinot'), ('Xinomavro', 'Xinomavro'), ('Žametovka', 'Žametovka'), ('Zinfandel / Crljenak Kaštelanski / Primitivo', 'Zinfandel / Crljenak Kaštelanski / Primitivo'), ('Zweigelt / Zweigeltrebe / Rotburger', 'Zweigelt / Zweigeltrebe / Rotburger'), ('Adalmiina', 'Adalmiina'), ('Addoraca', 'Addoraca'), ('Agh Shani', 'Agh Shani'), ('Aidani / Aidini / Aedani', 'Aidani / Aidini / Aedani'), ('Airén', 'Airén'), ('Alarije / Alarijen', 'Alarije / Alarijen'), ('Albalonga', 'Albalonga'), ('Albana', 'Albana'), ('Albanella', 'Albanella'), ('Albanello bianco', 'Albanello bianco'), ('Albaranzeuli bianco', 'Albaranzeuli bianco'), ('Albarello', 'Albarello'), ('Albariño / Alvarinho / Cainho branco', 'Albariño / Alvarinho / Cainho branco'), ('Albarola', 'Albarola'), ('Albillo', 'Albillo'), ('Alcañón', 'Alcañón'), ('Aligoté', 'Aligoté'), ('Alionza', 'Alionza'), ('Altesse / Roussette', 'Altesse / Roussette'), ('Amigne', 'Amigne'), ('Ansonica / Inzolia', 'Ansonica / Inzolia'), ('Antao Vaz', 'Antao Vaz'), ('Arany sárfehér / Izsáki', 'Arany sárfehér / Izsáki'), ('Arbane', 'Arbane'), ('Arbois', 'Arbois'), ('Arilla', 'Arilla'), ('Arinto / Assario branco', 'Arinto / Assario branco'), ('Arneis', 'Arneis'), ('Arnsburger', 'Arnsburger'), ('Arrufiac / Arrufiat / Ruffiac', 'Arrufiac / Arrufiat / Ruffiac'), ('Arvesiniadu', 'Arvesiniadu'), ('Asprinio bianco', 'Asprinio bianco'), ('Assyrtiko / Assyrtico', 'Assyrtiko / Assyrtico'), ('Athiri', 'Athiri'), ('Aubin / Aubin blanc', 'Aubin / Aubin blanc'), ('Aubin vert', 'Aubin vert'), ('Aurelius', 'Aurelius'), ('Auxerrois blanc', 'Auxerrois blanc'), ('Avesso', 'Avesso'), ('Azal branco', 'Azal branco'), ('Barcelo', 'Barcelo'), ('Bacchus', 'Bacchus'), ('Baco blanc', 'Baco blanc'), ('Baiyu / Rkatsiteli', 'Baiyu / Rkatsiteli'), ('Balzac blanc', 'Balzac blanc'), ('Banat Riesling / Banat Rizling', 'Banat Riesling / Banat Rizling'), ('Baratuciat', 'Baratuciat'), ('Barbera bianca', 'Barbera bianca'), ('Bariadorgia', 'Bariadorgia'), ('Baroque', 'Baroque'), ('Belina', 'Belina'), ('Benedino', 'Benedino'), ('Besgano bianco', 'Besgano bianco'), ('Bia blanc', 'Bia blanc'), ('Bianca', 'Bianca'), ('Biancame / Bianchello', 'Biancame / Bianchello'), ('Bianchetta Trevigiana', 'Bianchetta Trevigiana'), ('Bianchetti Genovese', 'Bianchetti Genovese'), ("Bianco d'Alessano", "Bianco d'Alessano"), ('Biancolella', 'Biancolella'), ('Biancu Gentile', 'Biancu Gentile'), ('Biancone di Portoferraio', 'Biancone di Portoferraio'), ('Bical / Borrado das Moscas', 'Bical / Borrado das Moscas'), ('Bigolona', 'Bigolona'), ('Blatterle', 'Blatterle'), ('Bratislavské biele', 'Bratislavské biele'), ('Boais', 'Boais'), ('Bogdanuša', 'Bogdanuša'), ('Bombino bianco', 'Bombino bianco'), ('Borba blanca', 'Borba blanca'), ('Bosco', 'Bosco'), ('Bourboulenc', 'Bourboulenc'), ('Bouvier', 'Bouvier'), ('Breidecker', 'Breidecker'), ('Brustiano bianco', 'Brustiano bianco'), ('Bual / Boal', 'Bual / Boal'), ('Budai Zöld', 'Budai Zöld'), ('Bukettraube', 'Bukettraube'), ('Burger / Monbadon', 'Burger / Monbadon'), ('Caíño blanco', 'Caíño blanco'), ('Camaralet', 'Camaralet'), ('Canari blanc', 'Canari blanc'), ('Caprettone', 'Caprettone'), ("Carica l'Asino", "Carica l'Asino"), ('Carignan blanc', 'Carignan blanc'), ('Cascarolo bianco', 'Cascarolo bianco'), ('Catarratto', 'Catarratto'), ('Cayetana / Calagraño / Jaén blanca / Garrido', 'Cayetana / Calagraño / Jaén blanca / Garrido'), ('Cereza', 'Cereza'), ('Chardonnay', 'Chardonnay'), ('Chasan', 'Chasan'), ('Chasselas / Fendant / Gutedel / Weisser Gutedel', 'Chasselas / Fendant / Gutedel / Weisser Gutedel'), ('Chenel', 'Chenel'), ('Chenin blanc / Pineau de la Loire / Steen', 'Chenin blanc / Pineau de la Loire / Steen'), ('Clairette', 'Clairette'), ('Claret de Gers / Claret de Gascogne', 'Claret de Gers / Claret de Gascogne'), ('Claverie', 'Claverie'), ('Cococciola', 'Cococciola'), ('Cocur', 'Cocur'), ('Coda di Pecora', 'Coda di Pecora'), ('Coda di Volpe / Guarnaccia bianca', 'Coda di Volpe / Guarnaccia bianca'), ('Colombard', 'Colombard'), ('Completer', 'Completer'), ('Cortese', 'Cortese'), ('Crato / Crato bianco', 'Crato / Crato bianco'), ('Courbu / Xuri Zerratua / Bordelesa Zuri', 'Courbu / Xuri Zerratua / Bordelesa Zuri'), ('Criolla Grande', 'Criolla Grande'), ('Crouchen / Clare Riesling / Cape Riesling', 'Crouchen / Clare Riesling / Cape Riesling'), ('Pearl of Csaba', 'Pearl of Csaba'), ('Cserszegi fűszeres', 'Cserszegi fűszeres'), ('Cygne blanc', 'Cygne blanc'), ('Dattier', 'Dattier'), ('Debina', 'Debina'), ('Debit', 'Debit'), ('Diagalves', 'Diagalves'), ('Dimiat', 'Dimiat'), ('Dinka', 'Dinka'), ('Doña Blanca', 'Doña Blanca'), ('Donzelinho branco', 'Donzelinho branco'), ('Doradilla (grape)', 'Doradilla (grape)'), ('Doradillo', 'Doradillo'), ('Drupeggio', 'Drupeggio'), ('Durella', 'Durella'), ('Ehrenfelser', 'Ehrenfelser'), ('Elbling', 'Elbling'), ('Emerald Riesling', 'Emerald Riesling'), ('Emir Karasi', 'Emir Karasi'), ('Encruzado', 'Encruzado'), ('Erbaluce', 'Erbaluce'), ('Esquitxagos', 'Esquitxagos'), ('Escanyavella', 'Escanyavella'), ('Ezerjó', 'Ezerjó'), ('Faber / Faberrebe', 'Faber / Faberrebe'), ('Falanghina', 'Falanghina'), ('False Pedro / Pedro Luis / Cañocazo', 'False Pedro / Pedro Luis / Cañocazo'), ('Farana', 'Farana'), ('Favorita', 'Favorita'), ('Fernao Pires / Fernão Pires', 'Fernao Pires / Fernão Pires'), ('Ferral', 'Ferral'), ('Fetească albă / Fetiaska / Leànyka', 'Fetească albă / Fetiaska / Leànyka'), ('Fetească regală', 'Fetească regală'), ('Fiano', 'Fiano'), ('Fié / Fiét / Fié gris', 'Fié / Fiét / Fié gris'), ('Findling', 'Findling'), ('Flora', 'Flora'), ('Fologosão', 'Fologosão'), ('Folle blanche / Gros Plant / Piquepoult', 'Folle blanche / Gros Plant / Piquepoult'), ('Forastera', 'Forastera'), ('Forastera (Spanish grape)', 'Forastera (Spanish grape)'), ('Francavida', 'Francavida'), ('Francusa', 'Francusa'), ('Freisamer / Freiburger', 'Freisamer / Freiburger'), ('Fromenteau', 'Fromenteau'), ('Furmint / Mosler / Sipon', 'Furmint / Mosler / Sipon'), ('Galego Dourado', 'Galego Dourado'), ('Garganega / Grecanico / Grecanio', 'Garganega / Grecanico / Grecanio'), ('Garnacha blanca / Grenache blanc', 'Garnacha blanca / Grenache blanc'), ('Gewürztraminer / Tramini / Traminac', 'Gewürztraminer / Tramini / Traminac'), ('Girgentina', 'Girgentina'), ('Giró blanc', 'Giró blanc'), ('Gloria', 'Gloria'), ('Godello', 'Godello'), ('Goldburger', 'Goldburger'), ('Goldriesling', 'Goldriesling'), ('Gouais blanc', 'Gouais blanc'), ('Graisse / Plant de Graisse', 'Graisse / Plant de Graisse'), ('Grasă de Cotnari', 'Grasă de Cotnari'), ('Grechetto', 'Grechetto'), ('Greco bianco', 'Greco bianco'), ('Green Hungarian', 'Green Hungarian'), ('Grenache gris', 'Grenache gris'), ('Grignolino', 'Grignolino'), ('Grillo / Riddu / Rossese bianco', 'Grillo / Riddu / Rossese bianco'), ('Grk Bijeli', 'Grk Bijeli'), ('Grolleau gris', 'Grolleau gris'), ('Gros Manseng / Izkiriota Handi', 'Gros Manseng / Izkiriota Handi'), ('Grüner Veltliner', 'Grüner Veltliner'), ('Guardavalle', 'Guardavalle'), ('Gutenborner', 'Gutenborner'), ('Hárslevelű', 'Hárslevelű'), ('Hondarrabi Zuri', 'Hondarrabi Zuri'), ('Humagne Blanche', 'Humagne Blanche'), ('Huxelrebe / Courtillier Musqué', 'Huxelrebe / Courtillier Musqué'), ('Incrocio Manzoni', 'Incrocio Manzoni'), ('Irsai Oliver / Irsay Oliver / Irsai Olivér', 'Irsai Oliver / Irsay Oliver / Irsai Olivér'), ('Italia', 'Italia'), ('Jacquère', 'Jacquère'), ('Jampal', 'Jampal'), ('Juhfark', 'Juhfark'), ('Juwel', 'Juwel'), ('Kanzler', 'Kanzler'), ('Keknyelu / Kéknyelű', 'Keknyelu / Kéknyelű'), ('Kerner', 'Kerner'), ('Knipperle / Klein Rauschling', 'Knipperle / Klein Rauschling'), ('Koshu', 'Koshu'), ("Karija l'Osü", "Karija l'Osü"), ('Krstač', 'Krstač'), ('Kujundžuša', 'Kujundžuša'), ('Ladikino', 'Ladikino'), ('Lado', 'Lado'), ('Lagarino bianco', 'Lagarino bianco'), ('Lagorthi', 'Lagorthi'), ('Lauzet', 'Lauzet'), ("Len de l'El / Len de l'Elh / Loin-de-l'oeil", "Len de l'El / Len de l'Elh / Loin-de-l'oeil"), ('Loureira', 'Loureira'), ('Luglienga', 'Luglienga'), ('Lumassina', 'Lumassina'), ('Macabeo / Macabeu / Viura', 'Macabeo / Macabeu / Viura'), ('Maceratino', 'Maceratino'), ('Madeleine Angevine', 'Madeleine Angevine'), ('Majarcă Albă', 'Majarcă Albă'), ('Malagousia / Malagoussia', 'Malagousia / Malagoussia'), ('Malvar / Lairén', 'Malvar / Lairén'), ('Malvasia, includes several sub-varieties', 'Malvasia, includes several sub-varieties'), ('Mantonico bianco', 'Mantonico bianco'), ('Manteudo', 'Manteudo'), ('Maria Gomes / Fernão Pires', 'Maria Gomes / Fernão Pires'), ('Marsanne', 'Marsanne'), ('Marzemina bianca', 'Marzemina bianca'), ('Mauzac', 'Mauzac'), ('Melon de Bourgogne / Muscadet', 'Melon de Bourgogne / Muscadet'), ('Merlot blanc', 'Merlot blanc'), ('Merseguera / Verdil / Verdosilla', 'Merseguera / Verdil / Verdosilla'), ('Meslier St-François', 'Meslier St-François'), ('Mezesfehér', 'Mezesfehér'), ('Minella bianca', 'Minella bianca'), ('Miousap', 'Miousap'), ('Molette', 'Molette'), ('Moll', 'Moll'), ('Montonico bianco', 'Montonico bianco'), ('Montu', 'Montu'), ('Morio-Muskat', 'Morio-Muskat'), ('Moscatel Rosada', 'Moscatel Rosada'), ('Moscato Giallo', 'Moscato Giallo'), ('Moschofilero / Moscophilero', 'Moschofilero / Moscophilero'), ('Mtsvane', 'Mtsvane'), ('Müller-Thurgau / Rivaner', 'Müller-Thurgau / Rivaner'), ('Muscadelle (Tokay in Australia)', 'Muscadelle (Tokay in Australia)'), ('Muscat / Moscato / Misket', 'Muscat / Moscato / Misket'), ('Muscat of Alexandria / Moscatell / Zibibbo / Moscatel de Málaga, de Setúbal', 'Muscat of Alexandria / Moscatell / Zibibbo / Moscatel de Málaga, de Setúbal'), ('Muscat Blanc à Petits Grains / Muscat Frontignan / Muskateller / Moscatel branco / Frontignan', 'Muscat Blanc à Petits Grains / Muscat Frontignan / Muskateller / Moscatel branco / Frontignan'), ('Muscat Ottonel', 'Muscat Ottonel'), ('Nasco', 'Nasco'), ('Neherleschol', 'Neherleschol'), ('Neuburger', 'Neuburger'), ('Nobling', 'Nobling'), ('Nosiola', 'Nosiola'), ('Nuragus', 'Nuragus'), ('Ondenc', 'Ondenc'), ('Optima', 'Optima'), ('Oraniensteiner', 'Oraniensteiner'), ('Orion', 'Orion'), ('Ortega', 'Ortega'), ('Ortrugo', 'Ortrugo'), ('Oz', 'Oz'), ('Pagedebit', 'Pagedebit'), ('Pálava', 'Pálava'), ('Pallagrello bianco', 'Pallagrello bianco'), ('Palomino / Listan / Perrum', 'Palomino / Listan / Perrum'), ('Pampanuto / Pampanino', 'Pampanuto / Pampanino'), ('Parč', 'Parč'), ('Pardillo / Pardina', 'Pardillo / Pardina'), ('Parellada', 'Parellada'), ('Pascal blanc', 'Pascal blanc'), ('Passerina', 'Passerina'), ('Pecorino / Pecorello', 'Pecorino / Pecorello'), ('Pedro Giménez', 'Pedro Giménez'), ('Pedro Ximénez/ PX / Alamís', 'Pedro Ximénez/ PX / Alamís'), ('Perle', 'Perle'), ('Petit Courbu', 'Petit Courbu'), ('Petit Manseng / Izkiriota Ttipi', 'Petit Manseng / Izkiriota Ttipi'), ('Petit Meslier', 'Petit Meslier'), ('Petite Arvine', 'Petite Arvine'), ('Picardin / Picardan / Aragnan blanc', 'Picardin / Picardan / Aragnan blanc'), ('Picolit / Piccolit / Piccolito', 'Picolit / Piccolit / Piccolito'), ('Picpoul / Piquepoul blanc / Piquepoul gris', 'Picpoul / Piquepoul blanc / Piquepoul gris'), ('Pigato', 'Pigato'), ('Pignerol', 'Pignerol'), ('Pignoletto', 'Pignoletto'), ('Pinella', 'Pinella'), ('Pinot blanc / Pinot bianco / Klevner / Weissburgunder', 'Pinot blanc / Pinot bianco / Klevner / Weissburgunder'), ('Pinot gris / Pinot grigio / Grauburgunder / Malvoisie / Pinot jaune / Szürkebarát', 'Pinot gris / Pinot grigio / Grauburgunder / Malvoisie / Pinot jaune / Szürkebarát'), ('Planta Fina', 'Planta Fina'), ('Planta Nova', 'Planta Nova'), ('Plavai / Plavay', 'Plavai / Plavay'), ('Pošip', 'Pošip'), ('Prensal', 'Prensal'), ('Prié blanc / Blanc de Morgex', 'Prié blanc / Blanc de Morgex'), ('Prosecco / Glera', 'Prosecco / Glera'), ('Prunesta', 'Prunesta'), ('Rabigato', 'Rabigato'), ('Rabo de Ovelha', 'Rabo de Ovelha'), ('Raisin blanc', 'Raisin blanc'), ('Rauschling / Rāuschling', 'Rauschling / Rāuschling'), ('Regner', 'Regner'), ('Reichensteiner', 'Reichensteiner'), ('Retagliado bianco', 'Retagliado bianco'), ('Rèze', 'Rèze'), ('Ribolla Gialla / Robola', 'Ribolla Gialla / Robola'), ('Riesling / Johannisberg Riesling / Rheinriesling / Klingelberger', 'Riesling / Johannisberg Riesling / Rheinriesling / Klingelberger'), ('Rieslaner', 'Rieslaner'), ('Rkatsiteli', 'Rkatsiteli'), ('Robola', 'Robola'), ('Roditis / Rhoditis', 'Roditis / Rhoditis'), ('Rollo', 'Rollo'), ('Romorantin', 'Romorantin'), ('Rossese bianco', 'Rossese bianco'), ('Roter Veltliner', 'Roter Veltliner'), ('Rotgipfler', 'Rotgipfler'), ('Roupeiro / Codega', 'Roupeiro / Codega'), ('Roussanne', 'Roussanne'), ('Rovello bianco', 'Rovello bianco'), ('Sabro', 'Sabro'), ('Sacy / Tresallier', 'Sacy / Tresallier'), ('Ste Marie', 'Ste Marie'), ('Saint-Pierre Doré', 'Saint-Pierre Doré'), ('Sarfeher / Sárfehér', 'Sarfeher / Sárfehér'), ('Sauvignon blanc / Sauvignon gris', 'Sauvignon blanc / Sauvignon gris'), ('Sauvignon vert / Sauvignonasse / Friulano / Tocai Friulano', 'Sauvignon vert / Sauvignonasse / Friulano / Tocai Friulano'), ('Savagnin / Savagnin blanc / Traminer', 'Savagnin / Savagnin blanc / Traminer'), ('Savatiano', 'Savatiano'), ('Scheurebe', 'Scheurebe'), ('Schönburger', 'Schönburger'), ('Sémillon', 'Sémillon'), ('Septiner', 'Septiner'), ('Sercial / Cerceal / Esgana Cão / Esgana', 'Sercial / Cerceal / Esgana Cão / Esgana'), ('Sereksia / Băbească albă', 'Sereksia / Băbească albă'), ('Sideritis', 'Sideritis'), ('Siegerrebe', 'Siegerrebe'), ('Silvaner / Sylvaner / Österreicher', 'Silvaner / Sylvaner / Österreicher'), ('Mátrai Muskotály', 'Mátrai Muskotály'), ('Smederevka', 'Smederevka'), ('Souvignier gris', 'Souvignier gris'), ('Spagnol', 'Spagnol'), ('Sultana', 'Sultana'), ('Sumoll Blanc', 'Sumoll Blanc'), ('Symphony', 'Symphony'), ('Tamarêz / Tamares / Crato branco', 'Tamarêz / Tamares / Crato branco'), ('Tamîioasa / Tămâioasă Românească / Tamianka', 'Tamîioasa / Tămâioasă Românească / Tamianka'), ('Taminga', 'Taminga'), ('Tempranillo blanco', 'Tempranillo blanco'), ('Téoulier', 'Téoulier'), ('Terrantez', 'Terrantez'), ('Terret gris', 'Terret gris'), ('Thrapsathiri', 'Thrapsathiri'), ('Timorasso', 'Timorasso'), ('Torrontés / Torontel / Moscatel de Austria', 'Torrontés / Torontel / Moscatel de Austria'), ('Tourbat / Torbato', 'Tourbat / Torbato'), ('Trbljan', 'Trbljan'), ('Trebbiano / Ugni blanc', 'Trebbiano / Ugni blanc'), ('Treixadura / Trajadura', 'Treixadura / Trajadura'), ('Trousseau gris / Grey Riesling', 'Trousseau gris / Grey Riesling'), ('Tsaoussi', 'Tsaoussi'), ('Tsolikauri', 'Tsolikauri'), ('Vega', 'Vega'), ('Verdea', 'Verdea'), ('Verdeca', 'Verdeca'), ('Verdejo', 'Verdejo'), ('Verdelho / Gouveio / Verdello', 'Verdelho / Gouveio / Verdello'), ('Verdello', 'Verdello'), ('Verdesse', 'Verdesse'), ('Verdicchio', 'Verdicchio'), ('Verdiso / Verdia', 'Verdiso / Verdia'), ('Verdoncho', 'Verdoncho'), ('Verduzzo', 'Verduzzo'), ('Verduzzo Trevigiano', 'Verduzzo Trevigiano'), ('Vermentino / Rolle', 'Vermentino / Rolle'), ('Vernaccia', 'Vernaccia'), ('Vernaccia di Oristano', 'Vernaccia di Oristano'), ('Veroga', 'Veroga'), ('Versoaln', 'Versoaln'), ('Vespaiola', 'Vespaiola'), ('Vidiano', 'Vidiano'), ('Vilana', 'Vilana'), ('Vinhao', 'Vinhao'), ('Viognier', 'Viognier'), ('Viosinho', 'Viosinho'), ('Vital (grape)', 'Vital (grape)'), ('Vitovska', 'Vitovska'), ('Voskehat', 'Voskehat'), ('Vugava', 'Vugava'), ('Weldra', 'Weldra'), ('Welschriesling / Riesling Italico / Olaszrizling / Lazki Rizling / Graševina', 'Welschriesling / Riesling Italico / Olaszrizling / Lazki Rizling / Graševina'), ('Würzer', 'Würzer'), ('Xarel·lo / Xarello', 'Xarel·lo / Xarello'), ('Xynisteri', 'Xynisteri'), ('Zala Gyöngye', 'Zala Gyöngye'), ('Zalema', 'Zalema'), ('Zefir', 'Zefir'), ('Zenit', 'Zenit'), ('Zengő', 'Zengő'), ('Zéta / Orémus', 'Zéta / Orémus'), ('Zeusz', 'Zeusz'), ('Zierfandler / Spätrot', 'Zierfandler / Spätrot'), ('Žilavka', 'Žilavka'), ('Žlahtina', 'Žlahtina'), ('Agdam Gyzyl Uzumu', 'Agdam Gyzyl Uzumu'), ('Chablais Rose', 'Chablais Rose'), ('Chardonnay Rose', 'Chardonnay Rose'), ('Gray Riesling Rose', 'Gray Riesling Rose'), ('Red Rose', 'Red Rose'), ('Zinfandel Rose', 'Zinfandel Rose')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='wine',
            name='vintage',
            field=models.PositiveIntegerField(default=1999),
        ),
    ]
