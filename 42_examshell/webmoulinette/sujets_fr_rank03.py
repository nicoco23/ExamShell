# -*- coding: utf-8 -*-
"""Traductions francaises des sujets de l'Exam Rank 03.

Servies a l'affichage par le serveur. Les metadonnees (fichier attendu,
fonctions autorisees, prototype) restent lues sur le sub.txt d'origine.
Les exemples de commandes/sorties et les squelettes de code sont conserves
tels quels.
"""

SUJETS = {}

# ============================== NIVEAU 1 ==============================

SUJETS["broken_gnl"] = """\
Nom                 : broken_GNL
Fichiers attendus   : get_next_line.c get_next_line.h
Fonctions autorisées: read, free, malloc
--------------------------------------------------------------------------------

Répare la fonction 'get_next_line' dans le fichier get_next_line.c, dont le
prototype doit être :

char *get_next_line(int fd);

Tu auras sans doute besoin de réparer d'autres fonctions également.

Description de la fonction 'get_next_line' :

Ta fonction doit renvoyer une ligne lue depuis le descripteur de fichier passé
en paramètre.

Une « ligne lue » est définie comme une suite de 0 à n caractères terminée par
un '\\n' (code ASCII 0x0a) ou par la fin de fichier (EOF).

La ligne doit être renvoyée avec son '\\n' s'il y en a un à la fin de la ligne
lue.

Quand tu atteins l'EOF, tu dois stocker le buffer courant dans un char * et le
renvoyer. Si le buffer est vide, tu dois renvoyer NULL.

En cas d'erreur, renvoie NULL.

Si tu ne renvoies pas NULL, le pointeur renvoyé doit être libérable (free).

Ton programme sera compilé avec le flag -D BUFFER_SIZE=xx, qui doit être utilisé
comme taille de buffer pour les appels à read dans tes fonctions.

Ta fonction ne doit pas fuir en mémoire.

Quand tu atteins l'EOF, ta fonction ne doit conserver aucune mémoire allouée par
malloc, à l'exception de la ligne renvoyée.

Appeler ta fonction get_next_line dans une boucle doit permettre de lire le
texte disponible sur un descripteur de fichier ligne par ligne jusqu'à la fin du
texte, quelle que soit la taille du texte ou de ses lignes.

Assure-toi que ta fonction se comporte correctement en lisant depuis un fichier,
depuis l'entrée standard, depuis une redirection, etc.

Aucun appel à une autre fonction ne sera fait sur le descripteur de fichier
entre deux appels à get_next_line.

Enfin, on considère que get_next_line a un comportement indéfini lorsqu'elle lit
un fichier binaire.
--------------------------------------------------------------------------------
"""

SUJETS["filter"] = """\
Nom                 : filter
Fichier attendu     : filter.c
Fonctions autorisées: read, write, strlen, memmem, memmove, malloc, calloc,
realloc, free, printf, fprintf, stdout, stderr, perror
--------------------------------------------------------------------------------

Écris un programme qui prend un et un seul argument.

Ton programme lira ensuite depuis stdin et écrira tout le contenu lu sur stdout,
sauf que chaque occurrence de s doit être remplacée par des '*' (autant que la
longueur de s). Ton programme sera testé avec des tailles de buffer aléatoires,
via une fonction read maison. Le buffer que tu utilises dans ton programme sera
donc rempli d'un nombre de caractères différent à chaque nouvel appel.

Par exemple :

./filter bonjour
se comportera exactement comme :
sed 's/bonjour/*******/g'

./filter abc
se comportera exactement comme :
sed 's/abc/***/g'

Plus généralement, ton programme doit être l'équivalent du script shell
filter.sh présent dans ce dossier (tu peux comparer ton programme avec lui).

En cas d'erreur pendant un read ou un malloc, tu dois écrire "Error: " suivi du
message d'erreur sur stderr et renvoyer 1.

Si le programme est appelé sans argument, avec un argument vide, ou avec
plusieurs arguments, il doit renvoyer 1.

Par exemple, ceci doit fonctionner :

$> echo 'abcdefaaaabcdeabcabcdabc' | ./filter abc | cat -e
***defaaa***de******d***$
$> echo 'ababcabababc' | ./filter ababc | cat -e
*****ab*****$
$>

NOTES :
memmem nécessite :
                #define _GNU_SOURCE
                #include <string.h>

perror nécessite :
                #include <errno.h>

read nécessite :
                #include <fcntl.h>
"""

SUJETS["scanf"] = """\
Nom                 : ft_scanf
Fichier attendu     : ft_scanf.c
Fonctions autorisées: fgetc, ungetc, ferror, feof, isspace, isdigit, stdin,
va_start, va_arg, va_copy, va_end
--------------------------------------------------------------------------------

Écris une fonction nommée `ft_scanf` qui imite le vrai scanf, avec les
contraintes suivantes :

- Elle ne gère que les conversions : s, d et c
- Tu n'as pas à gérer les options *, m et '
- Tu n'as pas à gérer la largeur de champ maximale
- Tu n'as pas à gérer les modificateurs de type (h, hh, l, etc.)
- Tu n'as pas à gérer les conversions commençant par %n$

Ta fonction doit être déclarée comme suit :

int ft_scanf(const char *, ... );

Tu trouveras dans ce dossier un fichier contenant une partie du code dont tu as
besoin, tu n'as plus qu'à le compléter.

Pour tester ton programme, compare tes résultats avec le vrai scanf.

Indice : tu auras sans doute besoin de lire le man de scanf.

#include <stdarg.h>
#include <stdio.h>
#include <ctype.h>

int match_space(FILE *f)
{
        // Tu peux insérer du code ici
    return (0);
}

int match_char(FILE *f, char c)
{
        // Tu peux insérer du code ici
    return (0);
}

int scan_char(FILE *f, va_list ap)
{
        // Tu peux insérer du code ici
    return (0);
}

int scan_int(FILE *f, va_list ap)
{
        // Tu peux insérer du code ici
    return (0);
}

int scan_string(FILE *f, va_list ap)
{
        // Tu peux insérer du code ici
    return (0);
}


int	match_conv(FILE *f, const char **format, va_list ap)
{
	switch (**format)
	{
		case 'c':
			return scan_char(f, ap);
		case 'd':
			match_space(f);
			return scan_int(f, ap);
		case 's':
			match_space(f);
			return scan_string(f, ap);
		case EOF:
			return -1;
		default:
			return -1;
	}
}

int ft_vfscanf(FILE *f, const char *format, va_list ap)
{
	int nconv = 0;

	int c = fgetc(f);
	if (c == EOF)
		return EOF;
	ungetc(c, f);

	while (*format)
	{
		if (*format == '%')
		{
			format++;
			if (match_conv(f, &format, ap) != 1)
				break;
			else
				nconv++;
		}
		else if (isspace(*format))
		{
			if (match_space(f) == -1)
				break;
		}
		else if (match_char(f, *format) != 1)
			break;
		format++;
	}
	
	if (ferror(f))
		return EOF;
	return nconv;
}


int ft_scanf(const char *format, ...)
{
	// ...
	int ret = ft_vfscanf(stdin, format, ap);
	// ...
	return ret;
}
"""

# ============================== NIVEAU 2 ==============================

SUJETS["n_queens"] = """\
Nom                 : n_queens
Fichiers attendus   : *.c *.h
Fonctions autorisées: atoi, fprintf, write, calloc, malloc, free, realloc,
stdout, stderr
--------------------------------------------------------------------------------

Écris un programme qui affiche toutes les solutions du problème des n reines
pour un n donné en argument.
Nous ne testerons pas avec des valeurs négatives.
L'ordre des solutions n'a pas d'importance.

Tu afficheras les solutions sous le format suivant :
<p1> <p2> <p3> ... \\n
où pn est l'indice de ligne de la reine dans chaque colonne, en partant de 0.

Par exemple, ceci doit fonctionner :
$> ./n_queens 2 | cat -e

$> ./n_queens 4 | cat -e
1 3 0 2$
2 0 3 1$

$> ./n_queens 7 | cat -e
0 2 4 6 1 3 5$
0 3 6 2 5 1 4$
etc...
"""

SUJETS["permutations"] = """\
Nom                 : permutations
Fichiers attendus   : *.c *.h
Fonctions autorisées: puts, malloc, calloc, realloc, free, write
--------------------------------------------------------------------------------

Écris un programme qui affiche toutes les permutations d'une chaîne donnée en
argument.

Les solutions doivent être données dans l'ordre alphabétique.

Nous n'essaierons pas ton programme avec des chaînes contenant des doublons
(ex : 'abccd').

Par exemple, ceci doit fonctionner :

$> ./permutations a | cat -e
a$

$> ./permutations ab | cat -e
ab$
ba$

$> ./permutations abc | cat -e
abc$
acb$
bac$
bca$
cab$
cba$
"""

SUJETS["powerset"] = """\
Nom                 : powerset
Fichiers attendus   : *.c *.h
Fonctions autorisées: atoi, printf, fprintf, malloc, calloc, realloc, free,
stdout, write
--------------------------------------------------------------------------------

Écris un programme qui prend en argument un entier n suivi d'un ensemble s
d'entiers distincts.
Ton programme doit afficher tous les sous-ensembles de s dont la somme des
éléments vaut n.

L'ordre des lignes n'a pas d'importance, mais l'ordre des éléments dans un
sous-ensemble, si : il doit correspondre à l'ordre dans l'ensemble initial s.
De cette manière, tu ne dois avoir aucun doublon (ex : '1 2' et '2 1').
Par exemple, avec la commande ./powerset 5 1 2 3 4 5
cette sortie est valide :
1 4
2 3
5
celle-ci l'est aussi :
2 3
5
1 4
mais pas celle-ci :
4 1
3 2
5

En cas d'erreur de malloc, ton programme doit quitter avec le code 1.

Nous ne testerons pas avec des ensembles invalides (par exemple '1 1 2').

Indice : l'ensemble vide est un sous-ensemble valide de tout ensemble. Il
s'affichera sous la forme d'une ligne vide.

Par exemple, ceci doit fonctionner :
$> ./powerset 3 1 0 2 4 5 3 | cat -e
3$
0 3$
1 2$
1 0 2$
$> ./powerset 12 5 2 1 8 4 3 7 11 | cat -e
8 4$
1 11$
1 4 7$
1 8 3$
2 3 7$
5 7$
5 4 3$
5 2 1 4$
$> ./powerset 0 1 -1 | cat -e
$
1 -1$
$> ./powerset 7 3 8 2 | cat -e

// Autres tests :
$> ./powerset 100 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 | cat -e
...
$> ./powerset -1 1 2 3 4 5 -10 | cat -e
...
$> ./powerset 0 -1 1 2 3 -2 | cat -e
...
$> ./powerset 13 65 23 3 4 6 7 1 2 | cat -e
...
$> ./powerset 10 0 1 2 3 4 5 6 7 8 9 | cat -e
...
"""

SUJETS["rip"] = """\
Nom                 : rip
Fichiers attendus   : *.c *.h
Fonctions autorisées: puts, write
--------------------------------------------------------------------------------

Écris un programme qui prend en argument une chaîne contenant uniquement des
parenthèses.
Si les parenthèses sont déséquilibrées (par exemple "())"), ton programme doit
retirer le nombre minimum de parenthèses pour que l'expression soit équilibrée.
« Retirer » signifie ici remplacer par des espaces.
Tu afficheras ensuite toutes les solutions (il peut y en avoir plusieurs).

L'ordre des solutions n'a pas d'importance.

Par exemple, ceci doit fonctionner :
$> ./rip '(()' | cat -e
 ()$
( )$
$> ./rip '((()()())())' | cat -e
((()()())())$
$> ./rip '()())()'| cat -e
()() ()$
()( )()$
( ())()$
$> ./rip '(()(()(' | cat -e
(()  ) $
( )( ) $
( ) () $
 ()( ) $
"""

SUJETS["tsp"] = """\
Nom                 : tsp
Fichiers attendus   : *.c *.h
Fonctions autorisées: write, sqrtf, getline, fseek, fscanf, ferror, feof,
fabsf, memcpy, fprintf, fclose, malloc, calloc, realloc, free, fopen,
errno, stderr, stdin, stdout
--------------------------------------------------------------------------------

La première publication désignant ce problème comme le « problème du voyageur de
commerce » se trouve dans un rapport de 1949 de la RAND Corporation, par Julia
Robinson : « On the Hamiltonian game (a traveling salesman problem) ».

Voici comment elle définit le problème :

« L'objet de cette note est de donner une méthode pour résoudre un problème lié
au problème du voyageur de commerce. Il semble utile de décrire le problème
d'origine. Une formulation consiste à trouver le trajet le plus court pour un
voyageur partant de Washington, visitant toutes les capitales d'État, puis
revenant à Washington.

Plus généralement : trouver la COURBE FERMÉE la plus courte contenant n points
donnés du plan. »

par exemple, avec l'ensemble de villes suivant :
0, 0
1, 0
2, 0
0, 1
1, 1
2, 1
1, 2
2, 2
que l'on peut représenter ainsi :
+ + +
+ + +
  + +
le chemin le plus court est :
 _____
|__   |
   |__|

donc tu dois afficher la longueur de ce chemin, soit :
8.00

Écris un programme qui lit un ensemble de coordonnées de villes sous la forme
'%f, %f\\n' depuis l'entrée standard et qui affiche la longueur du plus court
chemin possible contenant toutes ces villes, sous la forme '%.2f'.

Ton programme ne sera pas testé avec plus de 11 villes.

Tu trouveras dans ce dossier un fichier tsp.c contenant toutes les parties
ennuyeuses de cet exercice, ainsi que des fichiers d'exemple pour t'aider à
tester ton programme.

indice : pour utiliser sqrtf, ajoute -lm à la fin de ta commande de compilation.

Par exemple, ceci doit fonctionner :
$> cat square.txt
1, 1
0, 1
1, 0
0, 0
$> ./tsp < square.txt | cat -e
4.00$
"""
