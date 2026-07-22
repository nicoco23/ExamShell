# -*- coding: utf-8 -*-
"""Traductions françaises des sujets de l'Exam Rank 02.

Servies à l'affichage par le serveur. Les métadonnées (fichier attendu,
fonctions autorisées, prototype) restent lues sur le sub.txt d'origine.
Les exemples de commandes/sorties sont conservés tels quels.
"""

SUJETS = {}

# ============================== NIVEAU 0 ==============================

SUJETS["first_word"] = """\
Nom                 : first_word
Fichier attendu     : first_word.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et affiche son premier mot, suivi d'un
retour à la ligne.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne.

Si le nombre de paramètres n'est pas 1, ou s'il n'y a aucun mot, affiche
simplement un retour à la ligne.

Exemples :

$> ./first_word "FOR PONY" | cat -e
FOR$
$> ./first_word "this        ...    is sparta, then again, maybe    not" | cat -e
this$
$> ./first_word "   " | cat -e
$
$> ./first_word "a" "b" | cat -e
$
$> ./first_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
"""

SUJETS["fizzbuzz"] = """\
Nom                 : fizzbuzz
Fichier attendu     : fizzbuzz.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui affiche les nombres de 1 à 100, chacun séparé par un
retour à la ligne.

Si le nombre est un multiple de 3, il affiche 'fizz' à la place.
Si le nombre est un multiple de 5, il affiche 'buzz' à la place.
Si le nombre est à la fois multiple de 3 et de 5, il affiche 'fizzbuzz'.

Exemple :

$>./fizzbuzz
1
2
fizz
4
buzz
fizz
7
[...]
"""

SUJETS["ft_putstr"] = """\
Nom                 : ft_putstr
Fichier attendu     : ft_putstr.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris une fonction qui affiche une chaîne sur la sortie standard.

Le pointeur passé à la fonction contient l'adresse du premier caractère de la
chaîne.

Ta fonction doit être déclarée ainsi :

void	ft_putstr(char *str);
"""

SUJETS["ft_strcpy"] = """\
Nom                 : ft_strcpy
Fichier attendu     : ft_strcpy.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Reproduis le comportement de la fonction strcpy (man strcpy).

Ta fonction doit être déclarée ainsi :

char	*ft_strcpy(char *s1, char *s2);
"""

SUJETS["ft_strlen"] = """\
Nom                 : ft_strlen
Fichier attendu     : ft_strlen.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui renvoie la longueur d'une chaîne.

Ta fonction doit être déclarée ainsi :

int	ft_strlen(char *str);
"""

SUJETS["ft_swap"] = """\
Nom                 : ft_swap
Fichier attendu     : ft_swap.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui échange le contenu de deux entiers dont les adresses sont
passées en paramètres.

Ta fonction doit être déclarée ainsi :

void	ft_swap(int *a, int *b);
"""

SUJETS["repeat_alpha"] = """\
Nom                 : repeat_alpha
Fichier attendu     : repeat_alpha.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme nommé repeat_alpha qui prend une chaîne et l'affiche en
répétant chaque caractère alphabétique autant de fois que son rang dans
l'alphabet, suivi d'un retour à la ligne.

'a' devient 'a', 'b' devient 'bb', 'e' devient 'eeeee', etc.

La casse reste inchangée.

Si le nombre d'arguments n'est pas 1, affiche seulement un retour à la ligne.

Exemples :

$>./repeat_alpha "abc"
abbccc
$>./repeat_alpha "Alex." | cat -e
Alllllllllllleeeeexxxxxxxxxxxxxxxxxxxxxxxx.$
"""

SUJETS["rev_print"] = """\
Nom                 : rev_print
Fichier attendu     : rev_print.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et l'affiche à l'envers, suivie d'un
retour à la ligne.

Si le nombre de paramètres n'est pas 1, le programme affiche un retour à la
ligne.

Exemples :

$> ./rev_print "zaz" | cat -e
zaz$
$> ./rev_print "dub0 a POIL" | cat -e
LIOP a 0bud$
"""

SUJETS["rot_13"] = """\
Nom                 : rot_13
Fichier attendu     : rot_13.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et l'affiche en remplaçant chacune de ses
lettres par la lettre située 13 rangs plus loin dans l'ordre alphabétique.

'z' devient 'm' et 'Z' devient 'M'. La casse reste inchangée.

La sortie est suivie d'un retour à la ligne.

Si le nombre d'arguments n'est pas 1, le programme affiche un retour à la ligne.

Exemple :

$>./rot_13 "abc"
nop
$>./rot_13 "My horse is Amazing." | cat -e
Zl ubefr vf Nznmvat.$
"""

SUJETS["rotone"] = """\
Nom                 : rotone
Fichier attendu     : rotone.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et l'affiche en remplaçant chacune de ses
lettres par la suivante dans l'ordre alphabétique.

'z' devient 'a' et 'Z' devient 'A'. La casse reste inchangée.

La sortie est suivie d'un \\n.

Si le nombre d'arguments n'est pas 1, le programme affiche \\n.

Exemple :

$>./rotone "abc"
bcd
$>./rotone "AkjhZ zLKIJz , 23y " | cat -e
BlkiA aMLJKa , 23z $
"""

SUJETS["search_and_replace"] = """\
Nom                 : search_and_replace
Fichier attendu     : search_and_replace.c
Fonctions autorisées: write, exit
--------------------------------------------------------------------------------

Écris un programme nommé search_and_replace qui prend 3 arguments : le premier
est une chaîne dans laquelle remplacer une lettre (2e argument) par une autre
(3e argument).

Si le nombre d'arguments n'est pas 3, affiche seulement un retour à la ligne.

Si le deuxième argument n'est pas contenu dans le premier (la chaîne), le
programme réécrit simplement la chaîne suivie d'un retour à la ligne.

Note : les 2e et 3e arguments doivent être des caractères uniques.

Exemples :
$>./search_and_replace "Papache est un sabre" "a" "o"
Popoche est un sobre
$>./search_and_replace "zaz" "art" "zul" | cat -e
$
$>./search_and_replace "zaz" "r" "u" | cat -e
zaz$
"""

SUJETS["ulstr"] = """\
Nom                 : ulstr
Fichier attendu     : ulstr.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et inverse la casse de toutes ses
lettres. Les autres caractères restent inchangés.

Tu dois afficher le résultat suivi d'un '\\n'.

Si le nombre d'arguments n'est pas 1, le programme affiche '\\n'.

Exemple :

$>./ulstr "3:21 Ba  tOut  moUn ki Ka di KE m'en Ka fe fot" | cat -e
3:21 bA  ToUT  MOuN KI kA DI ke M'EN kA FE FOT$
"""

# ============================== NIVEAU 1 ==============================

SUJETS["alpha_mirror"] = """\
Nom                 : alpha_mirror
Fichier attendu     : alpha_mirror.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme nommé alpha_mirror qui prend une chaîne et l'affiche après
avoir remplacé chaque caractère alphabétique par le caractère alphabétique
opposé, suivi d'un retour à la ligne.

'a' devient 'z', 'Z' devient 'A', 'd' devient 'w', 'M' devient 'N', et ainsi de
suite.

La casse n'est pas changée.

Si le nombre d'arguments n'est pas 1, affiche seulement un retour à la ligne.

Exemples :

$>./alpha_mirror "abc"
zyx
$>./alpha_mirror "My horse is Amazing." | cat -e
Nb slihv rh Znzarmt.$
"""

SUJETS["camel_to_snake"] = """\
Nom                 : camel_to_snake
Fichier attendu     : camel_to_snake.c
Fonctions autorisées: malloc, free, realloc, write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne au format lowerCamelCase et la convertit
au format snake_case.

Une chaîne lowerCamelCase est une chaîne où chaque mot commence par une
majuscule, sauf le premier.

Une chaîne snake_case est une chaîne où chaque mot est en minuscules, séparé par
un underscore "_".

Exemples :
$>./camel_to_snake "hereIsACamelCaseWord"
here_is_a_camel_case_word
$>./camel_to_snake "helloWorld" | cat -e
hello_world$
"""

SUJETS["do_op"] = """\
Nom                 : do_op
Fichier attendu     : do_op.c
Fonctions autorisées: atoi, printf, write
--------------------------------------------------------------------------------

Écris un programme qui prend trois chaînes :
- La première et la troisième sont des représentations d'entiers signés en base
  10 qui tiennent dans un int.
- La deuxième est un opérateur arithmétique choisi parmi : + - * / %

Le programme doit afficher le résultat de l'opération demandée, suivi d'un retour
à la ligne. Si le nombre de paramètres n'est pas 3, le programme affiche
seulement un retour à la ligne.

Tu peux supposer que les chaînes ne contiennent pas d'erreurs ni de caractères
superflus. Les nombres négatifs auront un et un seul '-' en tête. Le résultat de
l'opération tient dans un int.

Exemples :

$> ./do_op "123" "*" 456 | cat -e
56088$
$> ./do_op "1" "+" "-43" | cat -e
-42$
"""

SUJETS["ft_atoi"] = """\
Nom                 : ft_atoi
Fichier attendu     : ft_atoi.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui convertit la chaîne str en un entier (type int) et le
renvoie.

Elle fonctionne comme la fonction standard atoi(const char *str), voir le man.

Ta fonction doit être déclarée ainsi :

int	ft_atoi(const char *str);
"""

SUJETS["ft_strcmp"] = """\
Nom                 : ft_strcmp
Fichier attendu     : ft_strcmp.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Reproduis le comportement de la fonction strcmp (man strcmp).

Ta fonction doit être déclarée ainsi :

int	ft_strcmp(char *s1, char *s2);
"""

SUJETS["ft_strcspn"] = """\
Nom                 : ft_strcspn
Fichier attendu     : ft_strcspn.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Reproduis exactement le comportement de la fonction strcspn (man strcspn).

La fonction doit renvoyer la longueur du plus long préfixe initial de s qui ne
contient aucun caractère de reject.

La fonction doit être prototypée ainsi :

size_t	ft_strcspn(const char *s, const char *reject);
"""

SUJETS["ft_strdup"] = """\
Nom                 : ft_strdup
Fichier attendu     : ft_strdup.c
Fonctions autorisées: malloc
--------------------------------------------------------------------------------

Reproduis le comportement de la fonction strdup (man strdup).

Ta fonction doit être déclarée ainsi :

char	*ft_strdup(char *src);
"""

SUJETS["ft_strrev"] = """\
Nom                 : ft_strrev
Fichier attendu     : ft_strrev.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui inverse (sur place) une chaîne de caractères.

Elle doit renvoyer son paramètre.

Ta fonction doit être déclarée ainsi :

char	*ft_strrev(char *str);
"""

SUJETS["inter"] = """\
Nom                 : inter
Fichier attendu     : inter.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend deux chaînes et affiche, sans doublons, les
caractères qui apparaissent dans les deux chaînes, dans l'ordre où ils
apparaissent dans la première.

L'affichage est suivi d'un \\n.

Si le nombre d'arguments n'est pas 2, le programme affiche \\n.

Exemples :

$>./inter "padinton" "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
padinto$
$>./inter "rien" "cette phrase ne cache rien" | cat -e
rien$
"""

SUJETS["is_power_of_2"] = """\
Nom                 : is_power_of_2
Fichier attendu     : is_power_of_2.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui détermine si un nombre donné est une puissance de 2.

Cette fonction renvoie 1 si le nombre donné est une puissance de 2, sinon 0.

Ta fonction doit être déclarée ainsi :

int	is_power_of_2(unsigned int n);
"""

SUJETS["last_word"] = """\
Nom                 : last_word
Fichier attendu     : last_word.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et affiche son dernier mot, suivi d'un
\\n.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne.

Si le nombre de paramètres n'est pas 1, ou s'il n'y a aucun mot, affiche un
retour à la ligne.

Exemple :

$> ./last_word "FOR PONY" | cat -e
PONY$
$> ./last_word "  lorem,ipsum  " | cat -e
lorem,ipsum$
"""

SUJETS["max"] = """\
Nom                 : max
Fichier attendu     : max.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris la fonction suivante :

int	max(int* tab, unsigned int len);

Le premier paramètre est un tableau d'int, le second est le nombre d'éléments du
tableau.

La fonction renvoie le plus grand nombre trouvé dans le tableau.

Si le tableau est vide, la fonction renvoie 0.
"""

SUJETS["print_bits"] = """\
Nom                 : print_bits
Fichier attendu     : print_bits.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris une fonction qui prend un octet et l'affiche en binaire, SANS retour à la
ligne à la fin.

Ta fonction doit être déclarée ainsi :

void	print_bits(unsigned char octet);

Exemple : si tu passes 2 à print_bits, elle affiche "00000010".
"""

SUJETS["reverse_bits"] = """\
Nom                 : reverse_bits
Fichier attendu     : reverse_bits.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui prend un octet, inverse son ordre bit à bit (comme dans
l'exemple) et renvoie le résultat.

Ta fonction doit être déclarée ainsi :

unsigned char	reverse_bits(unsigned char octet);

Exemple :
 0010 0110  ->  0110 0100
"""

SUJETS["snake_to_camel"] = """\
Nom                 : snake_to_camel
Fichier attendu     : snake_to_camel.c
Fonctions autorisées: malloc, free, realloc, write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne au format snake_case et la convertit au
format lowerCamelCase.

Une chaîne snake_case est une chaîne où chaque mot est en minuscules, séparé par
un underscore "_".

Une chaîne lowerCamelCase est une chaîne où chaque mot commence par une
majuscule, sauf le premier.

Exemples :
$>./snake_to_camel "here_is_a_snake_case_word"
hereIsASnakeCaseWord
$>./snake_to_camel "hello_world" | cat -e
helloWorld$
"""

SUJETS["swap_bits"] = """\
Nom                 : swap_bits
Fichier attendu     : swap_bits.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui prend un octet, échange ses deux moitiés (comme dans
l'exemple) et renvoie le résultat.

Ta fonction doit être déclarée ainsi :

unsigned char	swap_bits(unsigned char octet);

Exemple :
 0100 0001  ->  0001 0100
"""

SUJETS["union"] = """\
Nom                 : union
Fichier attendu     : union.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend deux chaînes et affiche, sans doublons, les
caractères qui apparaissent dans l'une ou l'autre des chaînes.

L'affichage se fait dans l'ordre où les caractères apparaissent sur la ligne de
commande, et est suivi d'un \\n.

Si le nombre d'arguments n'est pas 2, le programme affiche \\n.

Exemple :

$>./union zpadinton "paqefwtdjetyiytjneytjoeyjnejeyj" | cat -e
zpadintoqefwjy$
$>./union "rien" "cette phrase ne cache rien" | cat -e
rienct phas$
"""

SUJETS["wdmatch"] = """\
Nom                 : wdmatch
Fichier attendu     : wdmatch.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend deux chaînes et vérifie s'il est possible d'écrire
la première chaîne avec des caractères de la seconde, en respectant l'ordre dans
lequel ces caractères apparaissent dans la seconde.

Si c'est possible, le programme affiche la chaîne suivie d'un \\n, sinon il
affiche simplement un \\n.

Si le nombre d'arguments n'est pas 2, le programme affiche un \\n.

Exemples :

$>./wdmatch "faya" "fgvvfdxcacpolhyghbreda" | cat -e
faya$
$>./wdmatch "faya" "fgvvfdxcacpolhyghbred" | cat -e
$
"""

# ============================== NIVEAU 2 ==============================

SUJETS["add_prime_sum"] = """\
Nom                 : add_prime_sum
Fichier attendu     : add_prime_sum.c
Fonctions autorisées: write, exit
--------------------------------------------------------------------------------

Écris un programme qui prend un entier positif en argument et affiche la somme de
tous les nombres premiers inférieurs ou égaux à celui-ci, suivie d'un retour à la
ligne.

Si le nombre d'arguments n'est pas 1, ou si l'argument n'est pas un nombre
positif, affiche simplement 0 suivi d'un retour à la ligne.

Exemples :

$>./add_prime_sum 5
10
$>./add_prime_sum 7 | cat -e
17$
"""

SUJETS["epur_str"] = """\
Nom                 : epur_str
Fichier attendu     : epur_str.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et l'affiche avec exactement un espace
entre les mots, sans espace ni tabulation au début ni à la fin, suivie d'un \\n.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne.

Si le nombre d'arguments n'est pas 1, ou s'il n'y a aucun mot à afficher, le
programme affiche \\n.

Exemple :

$> ./epur_str " this        time it      will     be    more complex  . " | cat -e
this time it will be more complex .$
"""

SUJETS["expand_str"] = """\
Nom                 : expand_str
Fichier attendu     : expand_str.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et l'affiche avec exactement trois
espaces entre chaque mot, sans espace ni tabulation au début ni à la fin, suivie
d'un retour à la ligne.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne.

Si le nombre de paramètres n'est pas 1, ou s'il n'y a aucun mot, affiche
simplement un retour à la ligne.

Exemple :

$> ./expand_str " this        time it      will     be    more complex  " | cat -e
this   time   it   will   be   more   complex$
"""

SUJETS["ft_atoi_base"] = """\
Nom                 : ft_atoi_base
Fichier attendu     : ft_atoi_base.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui convertit la chaîne str (base N <= 16) en un entier
(base 10) et le renvoie.

Les caractères reconnus en entrée sont : 0123456789abcdef
Ils doivent bien sûr être tronqués selon la base demandée. Par exemple, la base
4 reconnaît "0123" et la base 16 reconnaît "0123456789abcdef".

Les majuscules doivent aussi être reconnues : "12fdb3" équivaut à "12FDB3".

Le signe moins ('-') n'est interprété que s'il est le premier caractère de la
chaîne.

Ta fonction doit être déclarée ainsi :

int	ft_atoi_base(const char *str, int str_base);
"""

SUJETS["ft_list_size"] = """\
Nom                 : ft_list_size
Fichier attendu     : ft_list_size.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui renvoie le nombre d'éléments de la liste chaînée qui lui
est passée.

Elle doit être déclarée ainsi :

int	ft_list_size(t_list *begin_list);

Tu dois utiliser la structure suivante dans ton fichier ft_list_size.c :

typedef struct    s_list
{
    struct s_list *next;
    void          *data;
}                 t_list;
"""

SUJETS["ft_range"] = """\
Nom                 : ft_range
Fichier attendu     : ft_range.c
Fonctions autorisées: malloc
--------------------------------------------------------------------------------

Écris la fonction suivante :

int	*ft_range(int start, int end);

Elle doit allouer (avec malloc()) un tableau d'entiers, le remplir de valeurs
consécutives allant de start à end (start et end inclus !), puis renvoyer un
pointeur vers la première valeur du tableau.

Exemples :
- Avec (1, 3) tu renvoies un tableau contenant 1, 2 et 3.
- Avec (0, -3) tu renvoies un tableau contenant 0, -1, -2 et -3.
"""

SUJETS["ft_rrange"] = """\
Nom                 : ft_rrange
Fichier attendu     : ft_rrange.c
Fonctions autorisées: malloc
--------------------------------------------------------------------------------

Écris la fonction suivante :

int	*ft_rrange(int start, int end);

Elle doit allouer (avec malloc()) un tableau d'entiers, le remplir de valeurs
consécutives allant de end à start (start et end inclus !), puis renvoyer un
pointeur vers la première valeur du tableau.

Exemples :
- Avec (1, 3) tu renvoies un tableau contenant 3, 2 et 1.
- Avec (0, -3) tu renvoies un tableau contenant -3, -2, -1 et 0.
"""

SUJETS["hidenp"] = """\
Nom                 : hidenp
Fichier attendu     : hidenp.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme nommé hidenp qui prend deux chaînes et affiche 1 suivi d'un
retour à la ligne si la première chaîne est cachée dans la seconde, sinon il
affiche 0 suivi d'un retour à la ligne.

Soit s1 et s2 deux chaînes. On dit que s1 est cachée dans s2 s'il est possible de
retrouver chaque caractère de s1 dans s2, dans le même ordre qu'ils apparaissent
dans s1. La chaîne vide est cachée dans n'importe quelle chaîne.

Si le nombre de paramètres n'est pas 2, le programme affiche un retour à la
ligne.

Exemples :

$>./hidenp "abc" "2altrb53c.sse" | cat -e
1$
$>./hidenp "abc" "btarc" | cat -e
0$
"""

SUJETS["lcm"] = """\
Nom                 : lcm
Fichier attendu     : lcm.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui prend deux unsigned int en paramètres et renvoie le PPCM
(plus petit commun multiple) calculé de ces paramètres.

Le PPCM de deux entiers non nuls est le plus petit entier positif divisible par
les deux entiers.

On peut le calculer via le PGCD :  PPCM(x, y) = | x * y | / PGCD(x, y)

Si au moins un des entiers est nul, le PPCM vaut 0.

Ta fonction doit être prototypée ainsi :

unsigned int	lcm(unsigned int a, unsigned int b);
"""

SUJETS["paramsum"] = """\
Nom                 : paramsum
Fichier attendu     : paramsum.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui affiche le nombre d'arguments qui lui sont passés, suivi
d'un retour à la ligne.

S'il n'y a aucun argument, affiche simplement 0 suivi d'un retour à la ligne.

Exemple :

$>./paramsum 1 2 3 5 7 24
6
$>./paramsum | cat -e
0$
"""

SUJETS["pgcd"] = """\
Nom                 : pgcd
Fichier attendu     : pgcd.c
Fonctions autorisées: printf, atoi, malloc, free
--------------------------------------------------------------------------------

Écris un programme qui prend deux chaînes représentant deux entiers strictement
positifs qui tiennent dans un int.

Affiche leur plus grand commun diviseur suivi d'un retour à la ligne (c'est
toujours un entier strictement positif).

Si le nombre de paramètres n'est pas 2, affiche un retour à la ligne.

Exemples :

$> ./pgcd 42 10 | cat -e
2$
$> ./pgcd 14 77 | cat -e
7$
"""

SUJETS["print_hex"] = """\
Nom                 : print_hex
Fichier attendu     : print_hex.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend un nombre positif (ou zéro) exprimé en base 10 et
l'affiche en base 16 (lettres minuscules) suivi d'un retour à la ligne.

Si le nombre de paramètres n'est pas 1, le programme affiche un retour à la
ligne.

Exemples :

$> ./print_hex "10" | cat -e
a$
$> ./print_hex "255" | cat -e
ff$
"""

SUJETS["rstr_capitalizer"] = """\
Nom                 : rstr_capitalizer
Fichier attendu     : rstr_capitalizer.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une ou plusieurs chaînes et, pour chaque argument,
met en majuscule la dernière lettre de chaque mot et le reste en minuscule, puis
affiche le résultat suivi d'un \\n.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne. Si un mot a une seule lettre, elle est mise en
majuscule.

Une lettre est un caractère de l'ensemble [a-zA-Z].

S'il n'y a aucun paramètre, affiche \\n.

Exemple :

$> ./rstr_capitalizer "a FiRSt LiTTlE TESt" | cat -e
A firsT littlE tesT$
"""

SUJETS["str_capitalizer"] = """\
Nom                 : str_capitalizer
Fichier attendu     : str_capitalizer.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui prend une ou plusieurs chaînes et, pour chaque argument,
met en majuscule le premier caractère de chaque mot (si c'est une lettre), met
le reste en minuscule, et affiche le résultat sur la sortie standard, suivi d'un
\\n.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne. Si un mot a une seule lettre, elle est mise en
majuscule.

S'il n'y a aucun argument, le programme affiche \\n.

Exemple :

$> ./str_capitalizer "a FiRSt LiTTlE TESt" | cat -e
A First Little Test$
"""

SUJETS["tab_mult"] = """\
Nom                 : tab_mult
Fichier attendu     : tab_mult.c
Fonctions autorisées: write
--------------------------------------------------------------------------------

Écris un programme qui affiche la table de multiplication d'un nombre.

Le paramètre sera toujours un nombre strictement positif qui tient dans un int,
et ce nombre multiplié par 9 tiendra aussi dans un int.

S'il n'y a aucun paramètre, le programme affiche \\n.

Exemple :

$>./tab_mult 9
1 x 9 = 9
2 x 9 = 18
[...]
9 x 9 = 81
"""

# ============================== NIVEAU 3 ==============================

SUJETS["flood_fill"] = """\
Nom                 : flood_fill
Fichier attendu     : flood_fill.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui prend un char ** (tableau de char à 2 dimensions), un
t_point pour les dimensions du tableau et un t_point pour le point de départ.

À partir du point 'begin' donné, cette fonction remplit toute une zone en
remplaçant les caractères qu'elle contient par le caractère 'F'. Une zone est un
groupe d'un même caractère délimité horizontalement et verticalement par
d'autres caractères ou par les bords du tableau.

flood_fill ne remplit pas en diagonale.

Prototype :
  void	flood_fill(char **tab, t_point size, t_point begin);

Structure t_point (à mettre dans flood_fill.c) :
  typedef struct  s_point
  {
    int           x;
    int           y;
  }               t_point;
"""

SUJETS["fprime"] = """\
Nom                 : fprime
Fichier attendu     : fprime.c
Fonctions autorisées: printf, atoi
--------------------------------------------------------------------------------

Écris un programme qui prend un entier positif et affiche ses facteurs premiers
sur la sortie standard, suivis d'un retour à la ligne.

Les facteurs doivent être affichés en ordre croissant et séparés par '*', de
sorte que l'expression obtenue donne le bon résultat.

Si le nombre de paramètres n'est pas 1, affiche simplement un retour à la ligne.

L'entrée, lorsqu'il y en a une, sera valide.

Exemples :

$> ./fprime 225225 | cat -e
3*3*5*5*7*11*13$
$> ./fprime 42 | cat -e
2*3*7$
$> ./fprime 1 | cat -e
1$
"""

SUJETS["ft_itoa"] = """\
Nom                 : ft_itoa
Fichier attendu     : ft_itoa.c
Fonctions autorisées: malloc
--------------------------------------------------------------------------------

Écris une fonction qui prend un int et le convertit en une chaîne terminée par
null. La fonction renvoie le résultat dans un tableau de char que tu dois
allouer.

Ta fonction doit être déclarée ainsi :

char	*ft_itoa(int nbr);
"""

SUJETS["ft_list_foreach"] = """\
Nom                 : ft_list_foreach
Fichiers attendus   : ft_list_foreach.c, ft_list.h
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris une fonction qui prend une liste et un pointeur de fonction, et applique
cette fonction à chaque élément de la liste.

Elle doit être déclarée ainsi :

void	ft_list_foreach(t_list *begin_list, void (*f)(void *));

La fonction pointée par f est utilisée ainsi :  (*f)(list_ptr->data);

Tu dois utiliser la structure suivante, à rendre dans un fichier ft_list.h :

typedef struct    s_list
{
    struct s_list *next;
    void          *data;
}                 t_list;
"""

SUJETS["ft_list_remove_if"] = """\
Nom                 : ft_list_remove_if
Fichier attendu     : ft_list_remove_if.c
Fonctions autorisées: free
--------------------------------------------------------------------------------

Écris une fonction nommée ft_list_remove_if qui retire de la liste passée tout
élément dont la donnée est « égale » à la donnée de référence.

Elle est déclarée ainsi :

void	ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)());

cmp prend deux void* et renvoie 0 quand les deux paramètres sont égaux.

Tu dois utiliser le fichier ft_list.h contenant :

typedef struct      s_list
{
    struct s_list   *next;
    void            *data;
}                   t_list;
"""

SUJETS["ft_split"] = """\
Nom                 : ft_split
Fichier attendu     : ft_split.c
Fonctions autorisées: malloc
--------------------------------------------------------------------------------

Écris une fonction qui prend une chaîne, la découpe en mots, et les renvoie sous
forme d'un tableau de chaînes terminé par NULL.

Un mot est une portion de chaîne délimitée soit par des espaces/tabulations/
retours à la ligne, soit par le début/la fin de la chaîne.

Ta fonction doit être déclarée ainsi :

char	**ft_split(char *str);
"""

SUJETS["rev_wstr"] = """\
Nom                 : rev_wstr
Fichier attendu     : rev_wstr.c
Fonctions autorisées: write, malloc, free
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne en paramètre et affiche ses mots dans
l'ordre inverse.

Un mot est une portion de chaîne délimitée par des espaces et/ou tabulations, ou
par le début/la fin de la chaîne.

Si le nombre de paramètres est différent de 1, le programme affiche '\\n'.

Dans les paramètres testés, il n'y aura pas d'espaces « superflus » (pas
d'espaces au début ni à la fin, et les mots sont séparés par exactement un
espace).

Exemples :

$> ./rev_wstr "You hate people! But I love gatherings. Isn't it ironic?" | cat -e
ironic? it Isn't gatherings. love I But people! hate You$
$> ./rev_wstr "Wingardium Leviosa" | cat -e
Leviosa Wingardium$
"""

SUJETS["rostring"] = """\
Nom                 : rostring
Fichier attendu     : rostring.c
Fonctions autorisées: write, malloc, free
--------------------------------------------------------------------------------

Écris un programme qui prend une chaîne et l'affiche après l'avoir tournée d'un
mot vers la gauche.

Ainsi, le premier mot devient le dernier, et les autres restent dans le même
ordre.

Un mot est une portion de chaîne délimitée par des espaces/tabulations, ou par
le début/la fin de la chaîne.

Les mots sont séparés par un seul espace dans la sortie.

S'il y a moins d'un argument, le programme affiche \\n.

Exemple :

$>./rostring "Que la      lumiere soit et la lumiere fut"
la lumiere soit et la lumiere fut Que
"""

SUJETS["sort_int_tab"] = """\
Nom                 : sort_int_tab
Fichier attendu     : sort_int_tab.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris la fonction suivante :

void	sort_int_tab(int *tab, unsigned int size);

Elle doit trier (sur place) le tableau d'int 'tab', qui contient exactement
'size' éléments, en ordre croissant.

Les doublons doivent être préservés.

L'entrée est toujours cohérente.
"""

SUJETS["sort_list"] = """\
Nom                 : sort_list
Fichier attendu     : sort_list.c
Fonctions autorisées: aucune
--------------------------------------------------------------------------------

Écris la fonction suivante :

t_list	*sort_list(t_list* lst, int (*cmp)(int, int));

Cette fonction doit trier la liste passée en paramètre en utilisant le pointeur
de fonction cmp pour choisir l'ordre à appliquer, et renvoie un pointeur vers le
premier élément de la liste triée.

Les doublons doivent rester. Les entrées sont toujours cohérentes.

Tu dois utiliser le type t_list décrit dans list.h et inclure ce fichier
(#include "list.h") sans le rendre.

Les fonctions passées comme cmp renvoient toujours une valeur différente de 0 si
a et b sont dans le bon ordre, 0 sinon. Exemple de cmp pour un tri croissant :

int ascending(int a, int b) { return (a <= b); }

Fichier list.h :
typedef struct s_list t_list;
struct s_list {
    int data;
    t_list *next;
};
"""
