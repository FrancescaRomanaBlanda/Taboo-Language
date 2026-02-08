## STEP 1. Define a Shared Analytical Frame ****

**On what grounds is taboo language problematized in each language,**

**and how do these grounds differ across linguistic and cultural contexts?**

- who is targeted (self, other, group, no target)
- how the expression functions (attack, emphasis, humor, regulation)
- how context affects its interpretation
- how social relationships shape its acceptability

---

## STEP 2. Language-Specific Analysis

Each language observes its own data → patterns are shared → patterns are compared

## 1️⃣ What each language team member does

*(Korean / Italian / Sinhala / English – same process for all)*

### Data Schema
1. sentence_id
    - string or int
2. Language
    - `ITA`
    - `KOR`
    - `SIN`
3. context
    - comment / sentence
    - the text unit on which offensiveness is judged
4. offensiveness
    - `OFF` : offensive
    - `NOT` : not offensive (including neutral or unspecified cases)
5. target_type
    - `UNT` : Untargeted
    - `IND` : Individual
    - `GRP` : Group
    - `OTH` : Other (organization, institution, event)
    - offensiveness = NOT→ `null`

6. target_group_attribute

- `Gender & Sexual Orientation`
- `Race, Ethnicity & Nationality`
- `Political Affiliation`
- `Religion`
- `Miscellaneous`
- defined only when `target_type = GRP`; otherwise `null`
1. offensive_span
    - Level A span he minimal and sufficient text span that justifies offensiveness
    - It can be tokens, word, expression..
    - that makes “context” offensive

###  Make or collect your own language

- **Existing datasets**
    - Do not assume consistency across sources
    - Check annotation purpose and unit (word, lemma, category)
- **Preprocessing & merging**
    - Normalize forms and labels
    - Remove duplicates, keep source info
    - Allow multi-label and ambiguous cases
- **EDA focus**
    - Frequency and category distribution
    - Single vs multi-category items
- **Balance**
    - Imbalance is expected and meaningful
    - Do not rebalance unless modeling requires it

## Criteria for Selecting Taboo Words (What to Focus On)

When collecting taboo-related words in your language, **do not aim for completeness**.

Instead, prioritize words that are **analytically rich** based on the following criteria.

### ① Function-Oriented Words

Select words that can serve **multiple communicative functions**, such as:

- interpersonal attack
- emotional release
- intensification
- joking or bonding
- evaluation of behavior or competence

👉 Words with **function flexibility** are more valuable than words with a single fixed use.

---

### ② Targetability

Prioritize words that can vary in **who or what they target**:

- the speaker (self-directed)
- another individual
- a group
- no explicit target (targetless use)

👉 Words that allow **target shifts or target deletion** are especially interesting.

---

### ③ Context Sensitivity

Focus on words whose taboo status:

- changes depending on context,
- speaker–listener relationship,
- tone or situation.

👉 Highly context-dependent words reveal how taboo meaning is **constructed**, not fixed.

---

### ④ Mitigation Likelihood

Select words that are often:

- softened,
- hedged, or
- accompanied by disclaimers or modifiers.

Examples:

- “kind of…”
- “a bit…”
- “I don’t mean to be rude, but…”

👉 Such words indicate **speaker awareness of social risk**.

---

### ⑤ Category Overlap Potential

Prioritize words that can plausibly belong to **multiple analytical categories**, such as:

- mental + intensifier
- offensive + joking
- general profanity + emotional regulation

👉 Words with frequent category overlap are key to understanding why taboo language resists clear-cut classification.

---

**for Sha-Shi :**

- translate my dataset and compare it with benchmark dataset (maybe in English)
- Original English Data vs Translated Data

### 🔹 (1) Observe taboo language **within your own language**

Each team member starts by **observing how taboo-related expressions are actually used** in their own language data.

Focus on questions like:

- Is the expression used as an **attack**, or as **emotional emphasis / intensification**?
- Does it function as a **serious insult**, or as **humor, irony, or bonding**?
- Is the taboo status determined by the **word itself**, or by the **context** (speaker, situation, target)?
- Does the expression serve a **social or pragmatic function** beyond literal meaning?
- Or other things (Embeddings, Statistics)

🚫 **No cross-language comparison at this stage**

✅ Only observe patterns *inside your own language*

---

### 🔸 Concrete examples (to clarify the task)

- **Korean example**
    - A mental-related expression meaning “crazy” may be used as:
        - a direct insult (towards a person), **or**
        - a casual intensifier (“That movie was crazy good”)
    - → The same word shifts function depending on context.

1️⃣ Taboo as an **Emotional Regulation Device** (Not an Attack)

- Traditional view: taboo = aggression
- Observed usage: **emotional release / stress regulation**

2️⃣ Taboo Neutralized by **Relational Closeness**

The meaning of taboo is not in the word itself,
but in the relationship between speakers.

- **Italian example**
    - An expression literally meaning “crazy” or “sick” may appear:
        - as a strong insult in some contexts,
        - but as playful exaggeration among friends.
    - → Observe when it becomes taboo and when it does not.
- **Sinhala example**
    - A taboo-related term may not be offensive by itself,
        - but becomes problematic only when directed at a specific person or group.
    - → The taboo status emerges from **who is targeted and how**.

👉 You are not judging correctness—only **observing usage patterns**.

---

### 🔹 (2) Loosely map observations to shared English categories

To enable later comparison, we use **English category names as labels**, not as standards.

Example category labels:

- *mental*
- *offensive*
- *sexual*
- *group-based*
- *general profanity*

Important rules:

- ❌ You do NOT need to choose only one category
- ⭕ Multiple categories can apply
- ⭕ If a case feels unclear, mark it as *ambiguous*

👉 Category mapping is **a descriptive note**, not a final decision.

---

### 🔸 Example of loose mapping

- A Korean expression:
    - mental + offensive (but sometimes joking)
- An Italian expression:
    - offensive + general profanity
- A Sinhala expression:
    - group-based only in specific contexts

Ambiguity is **expected and valuable**.

---

### 🔹 (3) Summarize internal patterns in your language

Each language team member prepares a short summary covering:

- Which categories feel **especially unclear or unstable** in this language
- Which categories **frequently overlap**
- Whether taboo status depends more on:
    - the **word itself**, or
    - the **context** (speaker, target, situation)

Short descriptive statements are enough.

---

### 🔸 Example summaries

- **Korean**
    
    > “Mental-related taboo expressions often function as intensifiers rather than direct insults.”
    > 
- **Italian**
    
    > “Some taboo expressions shift between offensive and playful meanings depending on familiarity between speakers.”
    > 
- **Sinhala**
    
    > “Taboo meaning is often determined by social hierarchy and target, rather than by the word alone.”
    > 

These statements are **results**, not hypotheses yet.

---

## 2️⃣ Pattern sharing & cross-language comparison

*(Team-level work)*

---

### 🔹 (4) Share observed patterns

Each team member briefly shares:

- “In my language, this kind of pattern appears…”

No debate yet—just sharing observations.

---

### 🔹 (5) Compare patterns across languages

Only at this stage does comparison begin.

Key questions:

- Does a similar pattern appear in other languages?
- Does it appear in a **different form**?
- Is it **strongly language- or culture-specific**?

👉 Differences are treated as **meaningful findings**, not inconsistencies.

## STEP 4. Interpretation (Cultural & Psychological)
