---
title: "System-Prompt-Vorlage: Spec Sheet → Werkzeug"
---

::: {.callout-note icon=false}
## Was du hier findest

Eine Vorlage, mit der du dein ausgefülltes Spec Sheet in einen System-Prompt für ein Chat-LLM übersetzst. Die Übersetzung ist mechanisch: du kopierst Inhalte aus den Sektionen B und C deines Spec Sheets in feste Platzhalter im Template.

Zwei Varianten sind unten beschrieben, je nachdem in welcher Rolle du das LLM einsetzen willst:

- **Diagnostische Rolle**: das LLM analysiert eine echte Lernenden-Antwort und identifiziert, welcher Wissensbaustein wahrscheinlich fehlt.
- **Lernende-Simulator**: das LLM spielt eine Lernende, der ein bestimmter Baustein fehlt, und produziert auf Anfrage Antworten.

Du fängst typischerweise mit der diagnostischen Rolle an. Der Lernende-Simulator ist für spätere Anwendungen, wenn du dein Spec Sheet schon kennst.
:::

::: {.callout-pro-tip icon=false}
## Spec ist dauerhaft, Prompt ist Übersetzung

Diese Vorlage ist ein **Ausgangspunkt**, nicht *die* Übersetzung. Die Form eines guten System-Prompts hängt vom konkreten Werkzeug und vom aktuellen Modellstand ab und ändert sich mit jeder Modellgeneration. Dein Spec Sheet bleibt gleich; die Übersetzung wird neu gerendert.

Zwei alternative Wege, dieselbe Übersetzung zu produzieren:

- **Aktuelle Anbieter-Dokumentation lesen.** Anthropic, OpenAI und andere veröffentlichen Prompt-Engineering-Guides für ihre Modelle ([docs.anthropic.com](https://docs.anthropic.com/), OpenAI Cookbook). Was dort steht, ändert sich häufiger als dein Spec Sheet.
- **Prompt-Generierungs-Tools nutzen.** Anthropic Console und OpenAI Playground haben Funktionen, mit denen du eine Beschreibung deiner Aufgabe (oder dein Spec Sheet) eingibst und einen strukturierten Prompt-Entwurf zurückbekommst. Das ist Rendering, nicht Spezifikation.

In allen drei Wegen bleibt dein Spec Sheet die dauerhafte Substanz. Was sich ändert, ist die Werkzeug-spezifische Übersetzung.
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

Wenn das Werkzeug nicht das tut, was du erwartet hast, geh **zurück zum Spec Sheet**. Häufig fehlt eine Information, die du im Spec Sheet noch nicht festgelegt hattest. Das ist eine zentrale Lehre aus Block 3: die Qualität des Prompts hängt an der Qualität des Spec Sheets.

## Variante 1: Diagnostische Rolle

**Wann nutzen:** du willst, dass das LLM dir hilft, Lernenden-Antworten daraufhin zu analysieren, welcher Wissensbaustein fehlt.

**Was es nicht ist:** ein automatisches Korrektursystem. Das LLM liefert eine Hypothese; du als Lehrperson entscheidest, ob sie zutrifft.

```{.markdown filename="system-prompt-diagnostisch.md"}
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

```{.markdown filename="system-prompt-lernende-simulator.md"}
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

## Hinweise zur Übersetzung

Drei wiederkehrende Schwierigkeiten:

- **Generizität vs. Spezifik.** Das LLM produziert standardmässig generische
  Antworten, die plausibel klingen. Im Prompt sollten die "Was
  schiefgeht"-Sätze aus deinem Spec Sheet wörtlich auftauchen.
- 
- **Konfabulationsdruck.** Das LLM ist trainiert, fluessige Antworten zu liefern. Die Verhaltensregel "scheitere realistisch" muss explizit dabei stehen, sonst spielt das Modell automatisch auf eine kompetentere Lernende um.

