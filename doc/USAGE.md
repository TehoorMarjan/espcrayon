# Utiliser le Bot

Le bot Twitch propose plusieurs commandes amusantes pour interagir.

## Le Crayon Lumineux

Vous pouvez piloter le crayon lumineux en utilisant la commande `!crayon` suivie
d'une couleur ou d'un effet. Plusieurs formats sont acceptés :

- Les valeurs rouge vert bleu séparées par des virgules :

  ```plaintext
  !crayon 255,0,0
  ```

- Le code hexadécimal CSS, à 3 ou 6 chiffres :

  ```plaintext
  !crayon #ff0000
  !crayon #f00
  ```

- Un nom de couleur prédéfinie (sans accents) :

  ```plaintext
  !crayon Rouge
  ```

- Un effet spécial :

  ```plaintext
  !crayon Rainbow
  ```

### Liste des Effets

| Nom     | Description                                                                                    |
| ------- | ---------------------------------------------------------------------------------------------- |
| Flicker | Simule une flamme vacillante, la couleur est identique à celle actuelle (peu visible en ligne) |
| Rainbow | Traverse doucement toutes les couleurs                                                         |
| Nodus   | Effet clin d'œil qui reprend les couleurs de la chaîne @no_dus                                 |

### Liste des Couleurs Prédéfinies

<table>
<tr><th>Nom</th><th>Couleur</th></tr>
<tr><td>Blanc</td><td style="background-color: #ffffff; width: 100px;">&nbsp;</td></tr>
<tr><td>Rouge</td><td style="background-color: #ff0000; width: 100px;">&nbsp;</td></tr>
<tr><td>Vermillon</td><td style="background-color: #ff1a02; width: 100px;">&nbsp;</td></tr>
<tr><td>Peche</td><td style="background-color: #ffc0b8; width: 100px;">&nbsp;</td></tr>
<tr><td>Barbie</td><td style="background-color: #ff866a; width: 100px;">&nbsp;</td></tr>
<tr><td>Corail</td><td style="background-color: #ff4401; width: 100px;">&nbsp;</td></tr>
<tr><td>Carotte</td><td style="background-color: #ff6a1c; width: 100px;">&nbsp;</td></tr>
<tr><td>Saumon</td><td style="background-color: #ff9257; width: 100px;">&nbsp;</td></tr>
<tr><td>Abricot</td><td style="background-color: #ff8b35; width: 100px;">&nbsp;</td></tr>
<tr><td>Tangerine</td><td style="background-color: #ff7f00; width: 100px;">&nbsp;</td></tr>
<tr><td>Orange</td><td style="background-color: #ff8811; width: 100px;">&nbsp;</td></tr>
<tr><td>Venitien</td><td style="background-color: #ffb95c; width: 100px;">&nbsp;</td></tr>
<tr><td>Beige</td><td style="background-color: #ffdca1; width: 100px;">&nbsp;</td></tr>
<tr><td>Melon</td><td style="background-color: #ffae19; width: 100px;">&nbsp;</td></tr>
<tr><td>Aurore</td><td style="background-color: #ffca60; width: 100px;">&nbsp;</td></tr>
<tr><td>Ocre</td><td style="background-color: #ffc832; width: 100px;">&nbsp;</td></tr>
<tr><td>Vanille</td><td style="background-color: #ffe9ae; width: 100px;">&nbsp;</td></tr>
<tr><td>Mais</td><td style="background-color: #ffde74; width: 100px;">&nbsp;</td></tr>
<tr><td>Miel</td><td style="background-color: #ffd10b; width: 100px;">&nbsp;</td></tr>
<tr><td>Or</td><td style="background-color: #ffd700; width: 100px;">&nbsp;</td></tr>
<tr><td>Paille</td><td style="background-color: #ffe347; width: 100px;">&nbsp;</td></tr>
<tr><td>Beurre</td><td style="background-color: #fff48d; width: 100px;">&nbsp;</td></tr>
<tr><td>Ecru</td><td style="background-color: #ffffe0; width: 100px;">&nbsp;</td></tr>
<tr><td>Ivoire</td><td style="background-color: #ffffd4; width: 100px;">&nbsp;</td></tr>
<tr><td>Flave</td><td style="background-color: #ffffa7; width: 100px;">&nbsp;</td></tr>
<tr><td>Soufre</td><td style="background-color: #ffff6b; width: 100px;">&nbsp;</td></tr>
<tr><td>Jaune</td><td style="background-color: #ffff00; width: 100px;">&nbsp;</td></tr>
<tr><td>Citron</td><td style="background-color: #f7ff3c; width: 100px;">&nbsp;</td></tr>
<tr><td>Chrome</td><td style="background-color: #edff0c; width: 100px;">&nbsp;</td></tr>
<tr><td>Chartreuse</td><td style="background-color: #c8ff33; width: 100px;">&nbsp;</td></tr>
<tr><td>Pistache</td><td style="background-color: #c5ff78; width: 100px;">&nbsp;</td></tr>
<tr><td>Lime</td><td style="background-color: #9fff38; width: 100px;">&nbsp;</td></tr>
<tr><td>Anis</td><td style="background-color: #aeff5d; width: 100px;">&nbsp;</td></tr>
<tr><td>Absinthe</td><td style="background-color: #92ff57; width: 100px;">&nbsp;</td></tr>
<tr><td>Amande</td><td style="background-color: #a9ff8c; width: 100px;">&nbsp;</td></tr>
<tr><td>Prairie</td><td style="background-color: #68ff46; width: 100px;">&nbsp;</td></tr>
<tr><td>Lichen</td><td style="background-color: #afffa6; width: 100px;">&nbsp;</td></tr>
<tr><td>Pomme</td><td style="background-color: #41ff2d; width: 100px;">&nbsp;</td></tr>
<tr><td>Vert</td><td style="background-color: #00ff00; width: 100px;">&nbsp;</td></tr>
<tr><td>Jade</td><td style="background-color: #93ff9d; width: 100px;">&nbsp;</td></tr>
<tr><td>Perroquet</td><td style="background-color: #3dff4f; width: 100px;">&nbsp;</td></tr>
<tr><td>Menthe</td><td style="background-color: #56ff90; width: 100px;">&nbsp;</td></tr>
<tr><td>Emeraude</td><td style="background-color: #01ff68; width: 100px;">&nbsp;</td></tr>
<tr><td>Opaline</td><td style="background-color: #acffe2; width: 100px;">&nbsp;</td></tr>
<tr><td>Turquoise</td><td style="background-color: #25ffea; width: 100px;">&nbsp;</td></tr>
<tr><td>Givre</td><td style="background-color: #9cffff; width: 100px;">&nbsp;</td></tr>
<tr><td>Aiguemarine</td><td style="background-color: #7cffff; width: 100px;">&nbsp;</td></tr>
<tr><td>Cyan</td><td style="background-color: #00ffff; width: 100px;">&nbsp;</td></tr>
<tr><td>Celeste</td><td style="background-color: #29d3ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Azurin</td><td style="background-color: #a9eaff; width: 100px;">&nbsp;</td></tr>
<tr><td>Auvergne</td><td style="background-color: #7adcff; width: 100px;">&nbsp;</td></tr>
<tr><td>Ceruleen</td><td style="background-color: #10acff; width: 100px;">&nbsp;</td></tr>
<tr><td>Fumee</td><td style="background-color: #d3eeff; width: 100px;">&nbsp;</td></tr>
<tr><td>Roi</td><td style="background-color: #369aff; width: 100px;">&nbsp;</td></tr>
<tr><td>Azur</td><td style="background-color: #007fff; width: 100px;">&nbsp;</td></tr>
<tr><td>Ciel</td><td style="background-color: #77b5ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Charrette</td><td style="background-color: #b6d0ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Electrique</td><td style="background-color: #2c75ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Pervenche</td><td style="background-color: #ccccff; width: 100px;">&nbsp;</td></tr>
<tr><td>Bleu</td><td style="background-color: #0000ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Majorelle</td><td style="background-color: #6f5cff; width: 100px;">&nbsp;</td></tr>
<tr><td>Lavande</td><td style="background-color: #a28dff; width: 100px;">&nbsp;</td></tr>
<tr><td>Persan</td><td style="background-color: #6500ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Indigo</td><td style="background-color: #7c1cff; width: 100px;">&nbsp;</td></tr>
<tr><td>Parme</td><td style="background-color: #e2afff; width: 100px;">&nbsp;</td></tr>
<tr><td>Lilas</td><td style="background-color: #dd7bff; width: 100px;">&nbsp;</td></tr>
<tr><td>Mauve</td><td style="background-color: #ff8aff; width: 100px;">&nbsp;</td></tr>
<tr><td>Magenta</td><td style="background-color: #ff00ff; width: 100px;">&nbsp;</td></tr>
<tr><td>Violet</td><td style="background-color: #ff1aaa; width: 100px;">&nbsp;</td></tr>
<tr><td>Fushia</td><td style="background-color: #ff0085; width: 100px;">&nbsp;</td></tr>
<tr><td>Bonbon</td><td style="background-color: #ff43a1; width: 100px;">&nbsp;</td></tr>
<tr><td>Macgowan</td><td style="background-color: #ff88ba; width: 100px;">&nbsp;</td></tr>
<tr><td>Rubis</td><td style="background-color: #ff136c; width: 100px;">&nbsp;</td></tr>
<tr><td>Rose</td><td style="background-color: #ff6c9f; width: 100px;">&nbsp;</td></tr>
<tr><td>Dragee</td><td style="background-color: #ffbfd2; width: 100px;">&nbsp;</td></tr>
<tr><td>Framboise</td><td style="background-color: #ff385c; width: 100px;">&nbsp;</td></tr>
<tr><td>Terracotta</td><td style="background-color: #ff6172; width: 100px;">&nbsp;</td></tr>
<tr><td>Vermeil</td><td style="background-color: #ff0821; width: 100px;">&nbsp;</td></tr>
<tr><td>Incarnadin</td><td style="background-color: #ff96a0; width: 100px;">&nbsp;</td></tr>
<tr><td>Grenadine</td><td style="background-color: #ff3d44; width: 100px;">&nbsp;</td></tr>
</table>