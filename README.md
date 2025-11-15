# 🧠 Daily Learning & Revision Agent  
### An AI-powered multi-agent system for personalized daily learning, revision, and knowledge retention.

---

## 📌 Overview

**Daily Learning & Revision Agent** is an intelligent multi-agent system designed to automate daily learning by generating structured study plans, personalized lessons, and revision quizzes—powered entirely by **Google Gemini**.

This project was built as part of the **Kaggle 5-Day AI Agents Intensive Capstone Project**, demonstrating practical agent architecture, tool use, memory management, and generative AI integration.

The system helps users learn any topic in a structured, multi-day format by:
- Breaking topics into daily subtopics  
- Generating high-quality lessons  
- Creating quiz questions for revision  
- Saving progress using long-term memory  
- Exporting daily lessons to Markdown  

---

## 🎯 Problem Statement

Learning consistently over multiple days can be difficult due to:
- Poorly structured study plans  
- Lack of personalized content  
- No automatic revision support  
- Difficulty tracking progress  

Most people struggle to maintain regular learning because the process is not automated, personalized, or adaptive.

---

## 🧩 Solution

The **Daily Learning & Revision Agent** automates the entire learning workflow using a multi-agent system powered by Gemini.

Given a topic and number of days:

1. **Planner Agent** creates a structured learning roadmap  
2. **Content Agent** generates daily lessons  
3. **Quiz Agent** produces revision questions  
4. **Memory Agent** logs progress and stores lessons/quizzes  
5. **Coordinator Agent** orchestrates the workflow  
6. **Loop Agent** runs daily cycles end-to-end  

This results in a fully autonomous personalized learning experience.

---

## 🏗️ Multi-Agent Architecture

                 ┌──────────────────────────┐
                 │        User Input        │
                 │    (Topic + No. of Days) │
                 └──────────────┬───────────┘
                                │
                                ▼
                 ┌──────────────────────────┐
                 │      Planner Agent       │
                 │  Generates daily roadmap │
                 └──────────────┬───────────┘
                                │
                        (Subtopic of Day)
                                │
     ┌──────────────────┬────────┴──────────┬───────────────────┬───────────────────┐
     ▼                  ▼                    ▼                   ▼
     ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐  ┌───────────────────┐
     │  Content Agent    │  │   Quiz Agent      │  │   Memory Agent    │  │   Export Tool     │
     │  Creates lessons  │  │  Generates Qs     │  │  Stores lessons & │  │  Generates MD     │
     │                   │  │                   │  │  progress         │  │  files            │
     └───────┬───────────┘  └───────┬───────────┘  └────────┬──────────┘  └────────┬──────────┘
             │                    │                       │                       │
             └────────────┬───────┴───────────────────────┴──────┬───────────────┘
                          ▼                                      ▼
                 ┌──────────────────────────────┐
                 │      Coordinator Agent       │
                 │   Orchestrates daily workflow│
                 └──────────────┬───────────────┘
                                ▼
                       ┌───────────────────┐
                       │     Loop Agent    │
                       │  Runs multi-day   │
                       │  learning process │
                       └───────────────────┘


---

### **What You Created — Overall Architecture**

The **Daily Learning & Revision Agent** is implemented as a modular, multi-agent system with sequential and autonomous flows. Each agent focuses on a single responsibility, and the system combines them into an automated daily learning pipeline.

#### **1. Coordinator Agent**  
Acts as the central controller. It receives user input (topic + number of days), activates sub-agents, manages sequencing, and ensures daily tasks are executed properly.

#### **2. Planner Agent**  
Uses Gemini to break the topic into structured daily modules, resulting in a personalized learning roadmap.

#### **3. Content Agent**  
Generates a complete lesson for the subtopic of the day using Gemini.  
The lesson includes:
- Introduction  
- Key concepts  
- Bullet points with explanations  
- Example/analogy  
- Summary  

#### **4. Quiz Agent**  
Creates daily revision questions based on the generated lesson.  
Questions help reinforce understanding and support active recall.

#### **5. Memory Agent**  
Stores:
- Daily lessons  
- Quizzes  
- Timestamps  
- Completion status  

This builds long-term context and enables better personalization.

#### **6. Export Tool**  
Saves generated lessons as Markdown files (`lesson_day_<n>.md`) for easy reading and offline revision.

#### **7. Loop Agent**  
Simulates multi-day progression and runs the entire learning workflow automatically for each day.

Together, these agents create a fully autonomous, personalized learning experience powered by Gemini.

---

### **Demo — How the System Works**

A typical workflow looks like this:

1. **User Input:**  
   `"Learn Machine Learning in 2 days"`

2. **Planner Agent:**  
   Breaks the topic into structured daily subtopics.

3. **Day 1 (Coordinator triggers sub-agents):**  
   - Content Agent → Generates Lesson 1  
   - Quiz Agent → Creates 6 revision questions  
   - Export Tool → Saves markdown file  
   - Memory Agent → Logs the day’s progress  

4. **Day 2:**  
   Same workflow repeats automatically via the Loop Agent.

#### **Sample Output Includes:**
- **Daily Lesson:**  
  Well-structured explanation using Gemini  
- **Quiz Questions:**  
  Personalized questions based on the day’s lesson  
- **Progress Log:**  
  Memory entries showing timestamps and daily completion  

The system behaves like an AI tutor that plans, teaches, evaluates, remembers, and prepares the next day’s lesson automatically.

---

### **The Build — Tools, Technologies & Approach**

- **Language & Platform:**  
  Python using a Kaggle Notebook environment.

- **Large Language Model:**  
  Gemini (`models/gemini-2.5-flash`) used for:  
  - Lesson creation  
  - Quiz generation  
  - Study plan creation  
  - Content summarization  

- **Multi-Agent Components:**  
  - Coordinator Agent  
  - Planner Agent  
  - Content Agent  
  - Quiz Agent  
  - Memory Agent  
  - Loop Agent  

- **Tools Used:**  
  - Markdown export tool  
  - Logging for observability  
  - JSON-based long-term memory  

- **Memory System:**  
  - Session-level memory (in-notebook state)  
  - Long-term memory (`memory_bank.json`)

- **Observability:**  
  Logging added for:  
  - Agent activations  
  - Memory updates  
  - Lesson/quiz generation  
  - Daily progress  

This build highlights **multi-agent intelligence, generative AI integration, memory, sequential pipelines, and long-running behavior**, aligning directly with the Kaggle Agents Intensive curriculum.

---

### **If I Had More Time…**

With more development time, the following enhancements would be added:

- Deploy the system using Cloud Run or Agent Engine  
- Build a web app for learners to track progress and interact with lessons  
- Add text-to-speech for audio-based lessons  
- Implement spaced repetition using memory embeddings  
- Enhance mastery tracking for weak concept detection  
- Generate diagrams, visuals, and videos to enrich lessons  
- Add cross-topic learning memory for long-term patterns  
- Push daily reminders and tasks to learners via notifications  

These improvements would transform the project into a full-fledged AI learning companion capable of long-term personalized education.

---
