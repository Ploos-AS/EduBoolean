# 54 – AND, OR og NOT i kode

Python bruker lesbare nøkkelord:

```python
can_enter = has_ticket and door_open
alarm = smoke or heat
safe = not alarm
```

C bruker:

```c
can_enter = has_ticket && door_open;
alarm = smoke || heat;
safe = !alarm;
```

Dette svarer konseptuelt til AND, OR og NOT fra boolsk algebra.

## Parenteser er din venn

Programmeringsspråk har presedensregler, men i undervisning og kompleks kode er eksplisitte parenteser ofte tydeligere:

```python
allowed = is_admin or (is_member and has_paid)
```

Neste: [if og kontrollflyt](55-if.md).
