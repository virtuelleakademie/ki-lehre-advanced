---
title: "Beispiel-Spec: Multiple Regression"
---

Vollständig ausgefülltes Beispiel-Spec zur Übung "Multiple Regression mit zwei Prädiktoren" aus Block 1. Du kannst dieses Beispiel als Vorlage für dein eigenes Spec verwenden, und du kannst es im Block 3 in das laufende Werkzeug einfügen, um zu sehen, was das Werkzeug damit produziert.

## Lernaufgabe (Kontext und Ziel)

**Wortlaut:** Die Lernenden führen in R eine multiple Regression mit zwei Prädiktoren durch und interpretieren das Ergebnis: Können Lernzeit ($X_1$) und Mathenote ($X_2$) gemeinsam die Klausurpunktzahl ($Y$) vorhersagen?

**Rahmen:** Übung 5 im Statistik-II-Kurs, im Anschluss an die einfache lineare Regression und die Partial-/Semipartialkorrelation. Lernende kennen $r$, $r^2$ und das Konzept der bivariaten Regression.

**Intendiertes Ergebnis:** Die Lernenden verstehen die konditionale Bedeutung der Aussage "kontrolliert für" und können einen Regressionskoeffizienten unter Berücksichtigung weiterer Prädiktoren angemessen interpretieren.

## Erforderliche Skills und Knowledge

- Konditionale Interpretation des Begriffs "kontrolliert für".
  *Erwerb:* zu erwerben (zentraler Lernziel-Baustein dieser Teilaufgabe).
  *Charakteristische Fehlerform:* Interpretation im Sinne einer experimentellen Manipulation oder eines rechnerischen "Herausrechnens".
- Differenzierung der Regressionskoeffizienten $b_1$ in bivariater versus multipler Regression.
  *Erwerb:* zu erwerben (Folge aus der Einführung der multiplen Regression).
  *Charakteristische Fehlerform:* Erwartung einer Identität der Koeffizienten über die Modelltypen hinweg.
- $R^2$ als gemeinsam erklärter Varianzanteil mehrerer Prädiktoren.
  *Erwerb:* zu erwerben (neu beim Übergang von einer auf mehrere Prädiktoren).
  *Charakteristische Fehlerform:* Additive Aufsummierung der bivariaten Bestimmtheitsmasse ($r^2_{YX_1} + r^2_{YX_2}$).
- Partial- und Semipartialkorrelation als unterschiedliche Konstrukte erkennen.
  *Erwerb:* vorausgesetzt (aus dem vorangegangenen Block); Verwechslung als Fehlerform bleibt diagnostisch relevant.
  *Charakteristische Fehlerform:* Verwechslung der beiden oder Reduktion auf eine einzige Kennzahl.
- Die Aussage des $t$-Tests pro Koeffizient korrekt formulieren.
  *Erwerb:* vorausgesetzt im Grundkonzept, in dieser Form zu erwerben (die Formulierung "unter Konstanthaltung des jeweils anderen Prädiktors" ist neu).
  *Charakteristische Fehlerform:* Aussagen über den Effekt insgesamt statt über den Effekt unter Konstanthaltung des jeweils anderen Prädiktors.
- Die Einheit eines Regressionskoeffizienten angeben.
  *Erwerb:* vorausgesetzt (aus bivariater Regression).
  *Charakteristische Fehlerform:* Standardisierte und unstandardisierte Koeffizienten miteinander verwechseln oder ohne Einheit interpretieren.

## Antizipierte Misconceptions

- Lernende konzeptualisieren das "Kontrollieren" als aktiven Eingriff in den Datensatz.
  *Vermutete intuitive Grundlage:* alltagssprachliche Konnotation des Begriffs "Kontrolle" als aktive Einflussnahme. Verstärkt durch sprachliche Formulierungen wie "rauspartialisieren" oder "herausrechnen".
- Lernende erwarten, dass Effekte über Modelltypen hinweg additiv und unverändert bleiben.
  *Vermutete intuitive Grundlage:* Übertragung von Linearitäts- und Separabilitäts-Heuristiken aus einfacheren Modellklassen, in denen Prädiktoren unkorreliert eingeführt wurden.
- Lernende interpretieren $R^2$ in der multiplen Regression als Summe der bivariaten $r^2$.
  *Vermutete intuitive Grundlage:* Übergeneralisierung der Additivität, die in der ANOVA-Varianzzerlegung mit orthogonalen Faktoren tatsächlich gilt.
- Lernende halten einen signifikanten bivariaten Zusammenhang für eine Garantie, dass der Prädiktor auch in der multiplen Regression signifikant bleibt.
  *Vermutete intuitive Grundlage:* implizite Annahme, dass Korrelationen zwischen Prädiktoren irrelevant für ihre individuellen Effekte sind.

## Hinweis

Dieses Spec ist ein Beispiel, kein vollständiges Modell der Aufgabe. Es ist die Hypothese einer Lehrperson nach einem Workshop-Lauf; nach Konfrontation mit realen Lernenden-Antworten würden vermutlich einzelne Skills geschärft, einige Misconceptions gestrichen und neue ergänzt.
