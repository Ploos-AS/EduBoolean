# Contributing to EduBoolean

EduBoolean is an educational project for complete beginners. Contributions should protect that goal.

## Core rule

**Never assume knowledge that the course has not already introduced.**

A technically correct explanation can still be pedagogically wrong if it requires unstated background knowledge.

## Language

- Norwegian is the primary language.
- English is a parallel course language.
- New Norwegian material does not have to wait for an English translation.
- English material should preserve the same learning objectives rather than blindly translating word for word.

## Lesson style

Prefer this progression:

1. familiar real-world situation
2. plain-language explanation
3. concrete examples
4. formal term
5. notation
6. truth table or diagram
7. practical use
8. exercises

Avoid introducing several new concepts in one paragraph when they can be separated.

## Examples

Examples should be:

- small enough to understand at a glance
- deterministic
- easy to reproduce
- free of unnecessary framework dependencies
- connected to real uses of Boolean logic

## Exercises

Answers should explain the reasoning. A bare answer such as `A = 1` is normally insufficient for beginner material.

## Source and licensing rules

See `LICENSES.md` before adding material.

Do not add copyrighted diagrams, book excerpts or third-party course material unless their license clearly permits reuse and the attribution/license requirements are satisfied.

## Software and simulator changes

The future EduLogic simulator should keep its evaluation core separate from its user interface. The logic core should be deterministic and testable without a GUI.

## Repository workflow

- `main` is canonical.
- Keep commits focused and descriptively named.
- Prefer small reviewable changes.
- Do not commit generated binary artifacts when they can be reproduced from source.
- Course sources are canonical; website/e-book/PDF outputs should be generated from them where practical.
