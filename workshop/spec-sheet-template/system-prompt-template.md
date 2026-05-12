---
title: "System-Prompt-Vorlage: Spec Sheet → Werkzeug"
---

::: {.callout-note icon=false}
## Was du hier findest

Eine Vorlage, mit der du dein ausgefülltes Spec Sheet in einen System-Prompt für ein Chat-LLM übersetzst. Die Übersetzung ist mechanisch: du kopierst Inhalte aus den Sektionen B und C deines Spec Sheets in feste Platzhalter im Template.

Drei Varianten sind unten beschrieben, je nachdem in welcher Rolle du das LLM einsetzen willst:

- **Diagnostische Rolle**: das LLM analysiert eine echte Lernenden-Antwort und identifiziert, welcher Wissensbaustein wahrscheinlich fehlt.
- **Lernende-Simulator**: das LLM spielt eine Lernende, der ein bestimmter Baustein fehlt, und produziert auf Anfrage Antworten.
- **Sokratischer Tutor**: das LLM stellt einer Lernenden Fragen, die einen bestimmten Baustein zur Selbstkonstruktion bringen.

Du fängst typischerweise mit der diagnostischen Rolle an. Die anderen sind für spätere Anwendungen, wenn du dein Spec Sheet schon kennst.
:::

::: {.callout-pro-tip icon=false}
## Spec ist dauerhaft, Prompt ist Übersetzung

Diese Vorlage ist ein **Ausgangspunkt**, nicht *die* Übersetzung. Die Form eines guten System-Prompts hängt vom konkreten Werkzeug und vom aktuellen Modellstand ab und ändert sich mit jeder Modellgeneration. Dein Spec Sheet bleibt gleich; die Übersetzung wird neu gerendert.

Zwei alternative Wege, dieselbe Übersetzung zu produzieren:

- **Aktuelle Anbieter-Dokumentation lesen.** Anthropic, OpenAI und andere veröffentlichen Prompt-Engineering-Guides für ihre Modelle ([docs.anthropic.com](https://docs.anthropic.com/), OpenAI Cookbook). Was dort steht, ändert sich häufiger als dein Spec Sheet.
- **Prompt-Generierungs-Tools nutzen.** Anthropic Console und OpenAI Playground haben Funktionen, mit denen du eine Beschreibung deiner Aufgabe (oder dein Spec Sheet) eingibst und einen strukturierten Prompt-Entwurf zurückbekommst. Das ist Rendering, nicht Spezifikation.

In allen drei Wegen bleibt dein Spec Sheet die durable Substanz. Was sich ändert, ist die Werkzeug-spezifische Übersetzung.
:::

::: {.callout-caution icon=false}
## Die Verbote in den Templates sind *soft constraints*

Sätze wie "erfinde keinen Wissensbaustein, der nicht oben gelistet ist" in den folgenden Varianten sind Bitten an das Modell, keine erzwungenen Constraints. Das Chat-Werkzeug prüft die Ausgabe nicht gegen das, was du im Prompt verlangt hast: das Modell hat keinen formalen Begriff von "der Liste oben". Die Klausel reduziert die Häufigkeit erfundener Bausteine in der Ausgabe, eliminiert sie nicht.

Wenn du eine harte Garantie brauchst (etwa für eine wiederkehrende Pipeline, in der manuelle Prüfung jeder Antwort unpraktikabel ist), gehört dasselbe Spec Sheet in einen **strukturierten API-Aufruf** statt in einen Chat-Prompt. Dort werden die Wissensbausteine als Enum definiert, und ein Schema-Validator weist jede Antwort mit einem Baustein-Wert ausserhalb des Enums zurück, bevor sie den Code erreicht. Das ist der Unterschied zwischen einem niedrigschwelligen Chat-Pfad mit weicher Klausel und einem strukturierten API-Pfad mit harter Schemaprüfung. Die konzeptuelle Erklärung dazu liegt unter [Strukturierter Output](../take-home/strukturierte-ausgabe.qmd); die konkrete Architektur des Block-3-Werkzeugs findest du im [Take-Home-Dokument zum Werkzeug](../take-home/api-werkzeug-erklaert.qmd).
:::

## So nutzt du die Vorlage

1. Wähle die passende Variante (siehe unten).
2. Kopiere das Template-Gerüst.
3. Ersetze die Platzhalter mit eckigen Klammern (`[...]`) durch Inhalte aus deinem Spec Sheet.
4. Füge das fertige Resultat als System-Prompt in dein Werkzeug ein (in Microsoft Copilot: "Anweisungen", in HuggingChat: "System Prompt", in ChatGPT: "Custom Instructions" oder Custom GPT, in Claude: "System Prompt").
5. Teste mit einer realen oder erfundenen Lernenden-Antwort.

Wenn das Werkzeug nicht das tut, was du erwartet hast, geh **zurück zum Spec Sheet**. Meistens fehlt eine Information, die du im Spec Sheet noch nicht festgelegt hattest. Das ist die wichtigste Lehre aus Block 3: die Qualität des Prompts ist eine Funktion der Qualität des Spec Sheets.

## Variante 1: Diagnostische Rolle

**Wann nutzen:** du willst, dass das LLM dir hilft, Lernenden-Antworten daraufhin zu analysieren, welcher Wissensbaustein fehlt.

**Was es nicht ist:** ein automatisches Korrektursystem. Das LLM liefert eine Hypothese; du als Lehrperson entscheidest, ob sie zutrifft.

```
Du bist eine Lehrassistentin, die einer Hochschuldozentin hilft, Antworten
von Lernenden zu analysieren.

Kontext der Aufgabe
-------------------

Teilaufgabe (Wortlaut):
[Inhalt von Sektion 1 (Wortlaut) deines Spec Sheets einfügen]

Kurskontext:
[Inhalt von Sektion 1 (Rahmen) einfügen]

Lernziel der Teilaufgabe:
[Inhalt von Sektion 1 (Lernziel) einfügen]

Wissensbausteine, die diese Teilaufgabe verlangt
-------------------------------------------------

Faktenwissen:
[Liste der Faktenwissen-Bausteine aus Sektion 2, je mit "Was schiefgeht"-Satz]

Klassifikationswissen:
[Liste der Klassifikations-Bausteine, je mit "Was schiefgeht"-Satz]

Erklärungswissen:
[Liste der Erklärungs-Bausteine, je mit "Was schiefgeht"-Satz]

Wahrscheinliche Fehlkonzepte
-----------------------------

[Liste aus Sektion 3 deines Spec Sheets, je in Ich-Form, mit Typ und
"Diskriminiert die Aufgabe?"-Notiz]

Deine Aufgabe
-------------

Wenn ich dir eine Lernenden-Antwort gebe, mache folgendes:

1. Identifiziere höchstens DREI Wissensbausteine oder Fehlkonzepte aus den
   Listen oben, die in der Antwort am ehesten betroffen sind. Begründe je
   in einem Satz, anhand welcher Stelle in der Antwort du das siehst.

2. Gib für jeden identifizierten Punkt eine kurze beobachtbare Spur:
   wörtlich zitiertes oder paraphrasiertes Material aus der Antwort.

3. Schlage zum Schluss EINE Intervention vor: eine konkrete Frage, ein
   Beispiel oder eine Übung, die diesen Wissensbaustein adressiert.
   Bitte konkret und auf den Kurskontext zugeschnitten.

Wichtige Einschränkungen
------------------------

- Wenn du keinen Punkt aus den Listen klar erkennst, sag das. Erfinde
  keinen Wissensbaustein, der nicht oben gelistet ist.
- Wenn die Antwort der Lernenden für die Teilaufgabe insgesamt korrekt
  ist, sag das einfach. Suche nicht nach Fehlern, wo keine sind.
- Spiele kein künstlich überhöhtes oder vermindertes Selbstvertrauen.
  Sage "ich bin unsicher", wenn du es bist.
- Antworte auf Deutsch.
```

::: {.callout-pro-tip icon=false}
## Tipp zum Testen

Teste den fertigen Prompt mit einer Lernenden-Antwort, von der du selbst weisst, welcher Baustein fehlt. Wenn das LLM den Baustein zuverlässig identifiziert: gut. Wenn nicht: schau in deinem Spec Sheet, ob die Beschreibung des Bausteins (insbesondere die "Was schiefgeht"-Felder) konkret genug ist. Meistens hilft es, dort zu schärfen.
:::

## Variante 2: Lernende-Simulator

**Wann nutzen:** du willst eine Aufgabe vor dem Einsatz mit Lernenden testen, indem du Antworten von Lernenden mit verschiedenen Bausteinlücken simulieren lässt.

```
Du übernimmst die Rolle einer Lernenden auf folgendem Niveau:

Kurskontext:
[Inhalt von Sektion 1 (Rahmen) einfügen]

Du bist auf diesem Niveau eine sonst kompetente Lernende. Was du
allerdings noch *nicht* hast:

[Wähle einen Baustein aus Sektion 2 deines Spec Sheets und füge ein:
Name + Typ + "Was schiefgeht, wenn er fehlt"-Beschreibung]

oder, alternativ, ein Fehlkonzept:

[Wähle ein Fehlkonzept aus Sektion 3: Aussage in Ich-Form + intuitive Basis]

Was du auch noch hast (typische andere Bausteine auf deinem Niveau):

[Liste der anderen Bausteine aus Sektion 2, falls du das LLM auf "kompetent
ausser im genannten Punkt" festlegen willst]

Verhaltensregeln
----------------

- Antworte auf Aufgaben so, wie diese Lernende sie beantworten würde.
- Spiele weder absichtlich dumm noch absichtlich klug. Bleibe in der
  spezifizierten Rolle.
- Wenn die Aufgabe genau den fehlenden Baustein abfragt, scheitere
  realistisch: nicht durch Schweigen, sondern durch eine plausibel-falsche
  oder fluessig-aber-falsche Antwort.
- Wenn die Aufgabe einen anderen Baustein abfragt, antworte korrekt.
- Antworte auf Deutsch.
- Brich nicht aus der Rolle aus, auch wenn ich dich direkt frage. Wenn ich
  schreibe "spiel mal die richtige Antwort", schreib trotzdem als die
  spezifizierte Lernende.
```

## Variante 3: Sokratischer Tutor (optional)

**Wann nutzen:** für Aufgaben, in denen die Lernende einen Erklärungsbaustein selbst konstruieren soll. Diese Variante ist riskanter: das LLM neigt dazu, abzukürzen und die Antwort selbst zu liefern. Brauche sie nur, wenn dein Spec Sheet einen klaren Erklärungs-Baustein hat, dessen Konstruktion du unterstützen willst.

```
Du bist eine sokratische Lernbegleiterin für eine Lernende, die folgenden
Erklärungs-Baustein selbst aufbauen soll:

Erklärungs-Baustein:
[Name aus Sektion 2 + die "Was schiefgeht"-Beschreibung einfügen]

Kurskontext:
[Sektion 1 (Rahmen) einfügen]

Verhalten
---------

- Stelle Fragen, die die Lernende zu einer eigenen Festlegung bringen.
  Eigene Festlegung heisst: eine Aussage, die richtig oder falsch sein
  könnte und für die die Lernende einsteht.
- Beantworte die Frage NICHT für sie. Auch nicht, wenn die Lernende
  direkt um die Antwort bittet.
- Wenn die Lernende eine Festlegung produziert, die teilweise stimmt,
  greife einen konkreten Aspekt heraus und frag nach der Begründung.
- Wenn die Lernende eine Festlegung produziert, die ein bekanntes
  Fehlkonzept reflektiert (siehe unten), führe ein kontrastives Beispiel
  ein, das das Fehlkonzept zum Scheitern bringt. Beantworte aber weiterhin
  nicht direkt.
- Maximal vier Fragen, dann eine Einladung zur Selbsteinschätzung: "Wie
  würdest du diese Aufgabe einer Mitstudierenden in einem Satz erklären?"

Bekannte Fehlkonzepte (auf die du achten solltest, ohne sie direkt zu
benennen):

[Liste aus Sektion 3 deines Spec Sheets, in Ich-Form]

- Antworte auf Deutsch.
- Halte deine Repliken kurz: eine bis drei Sätze pro Replik.
```

## Hinweise zur Übersetzung

**Was die Übersetzung schwer macht:** dein Spec Sheet ist deklarativ ("der Baustein 'kennt $-1 \le r \le 1$' ist Faktenwissen"). Der System-Prompt ist instruktiv ("verhalte dich so, dass..."). Die Übersetzung muss die deklarativen Aussagen in Verhaltensregeln umsetzen, die das LLM versteht.

Drei wiederkehrende Schwierigkeiten:

- **Generizität vs. Spezifik.** Das LLM produziert standardmässig generische Antworten, die plausibel klingen. Im Prompt müssen die "Was schiefgeht"-Sätze aus deinem Spec Sheet wörtlich auftauchen, sonst greift die Spezifik nicht.
- **Konfabulationsdruck.** Das LLM ist trainiert, fluessige Antworten zu liefern. Die Verhaltensregel "scheitere realistisch" muss explizit dabei stehen, sonst spielt das Modell automatisch auf eine kompetentere Lernende um.
- **Rollen-Stabilität.** Insbesondere die Tutor-Rolle bricht oft zusammen, wenn die Nutzerin direkt um die Antwort bittet. Die "Brich nicht aus der Rolle aus"-Klausel hilft, ist aber nicht garantiert wirksam. Test immer mit so einem Fall.

**Werkzeug-spezifische Eigenheiten:**

- **Microsoft Copilot:** akzeptiert lange System-Prompts. Achtung mit der "Web-Suche"-Funktion: schalte sie ab, wenn du willst, dass das LLM nur aus deinem Prompt zieht.
- **HuggingChat:** unterstützt System-Prompts, aber unterschiedliche Modelle reagieren unterschiedlich gut auf die Verhaltensregeln. Probiere zuerst Llama-Instruct- oder Qwen-Modelle.
- **ChatGPT (Custom GPT):** das Anweisungs-Feld ist auf 8000 Zeichen begrenzt. Bei längeren Spec Sheets musst du komprimieren.
- **Claude:** akzeptiert lange System-Prompts und folgt den Verhaltensregeln in der Regel zuverlässiger als andere Modelle.

## Wenn der Prompt nicht funktioniert

Symptom-Diagnose:

- **Das LLM produziert generischen Text.** Im Prompt fehlt die Spezifik aus deinem Spec Sheet (insbesondere die "Was schiefgeht"-Sätze). Geh zurück zur Sektion 2 und schärfe die Beschreibungen.
- **Das LLM identifiziert immer denselben Baustein.** Wahrscheinlich überlappen mehrere Bausteine im Spec Sheet. Geh zurück und prüfe, ob du sie schärfer trennen kannst.
- **Das LLM bricht aus der Rolle aus** (bei Variante 2 oder 3). Die Verhaltensregel ist nicht stark genug formuliert, oder das Modell ist auf "hilfreich" getuned, ohne Rollenstabilität. Teste mit einem anderen Modell oder verstärke die Klausel.
- **Das LLM ist zu pedantisch.** Du hast wahrscheinlich zu viele Verbote eingebaut. Reduziere sie auf die zwei oder drei wichtigsten.

In jedem Fall ist der erste Reflex: zurück zum Spec Sheet, nicht der Prompt umformulieren. Der Prompt ist Rendering, das Spec Sheet ist Substanz.
