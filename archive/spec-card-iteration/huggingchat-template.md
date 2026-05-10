---
title: "Tier 2: HuggingChat-Template"
---

::: {.callout-note icon=false}
Das Template für die Tier-2-Demo. Praktisch identisch mit dem Copilot-Template: dieselbe Spec Card, dieselbe JSON-Spezifikation. Was sich ändert, ist das Modell darunter und sein Standardverhalten.
:::

## Warum HuggingChat dabei ist

- **Modellunabhängigkeit:** HuggingChat läuft auf Open-Weight-Modellen (Llama, Mistral, Qwen). Wenn deine Spec Card hier funktioniert, ist sie nicht an einen Anbieter gebunden.
- **Kein Account-Zwang:** HuggingChat ist ohne Login nutzbar (mit Limitationen). Damit kannst du die Diagnose-Funktion auch dort einsetzen, wo du keine institutionelle Lizenz hast.
- **Diagnose der Spec Card durch Modellvergleich:** wenn dieselbe Spec Card auf einem Open-Weight-Modell deutlich anders antwortet als auf Copilot oder Claude, lernst du etwas über *deine Spec Card*, nicht über die Modelle.

## Wie du es benutzt

1. Gehe auf [huggingface.co/chat](https://huggingface.co/chat).
2. Wähle ein Modell, das System-Prompts unterstützt (die meisten neueren Open-Weight-Chat-Modelle tun das).
3. Öffne die Modell-Einstellungen und setze den unten stehenden Block als System-Prompt.
4. Sende die Studierendenantwort als erste Nachricht.

## Das Template (kopieren und einfügen)

Identisch zum [Copilot-Template](copilot-template.md). Die Spec Card ist werkzeugunabhängig, das ist der Punkt.

## Worauf in der Demo zu achten ist

- Open-Weight-Modelle sind oft weniger aggressiv RLHF-trainiert. Sie *halten* sich oft genauer an deine Rolle (gut), aber sie *konfabulieren* auch fluenter (schlecht). Das Verbot "generiere keine plausibel klingenden Texte, um fehlende Schemata zu überspielen" wird hier wichtiger als bei Copilot.
- Manche Open-Weight-Modelle ignorieren System-Prompts unter Druck, besonders wenn der User-Prompt sehr lang ist. Du wirst sehen, wo das passiert.
- Kleinere Modelle (etwa 7B-Parameter) verstehen Spec Cards mit vielen Sektionen oft schlecht. Wenn HuggingChat hier schlechter abschneidet als Copilot, kann es am Modell liegen, nicht an deiner Spec Card.

## Was die Demo zeigt

Wenn die *gleiche* Spec Card auf Copilot und auf HuggingChat *konsistente* Diagnosen produziert, ist deine Spec Card sauber spezifiziert. Wenn die Diagnosen *systematisch abweichen*, hast du eine Lücke gefunden, an der die Modell-Defaults das Verhalten bestimmen, weil deine Spec dort nichts gesagt hat. Das ist die Stelle, an der du nachschärfen musst.
