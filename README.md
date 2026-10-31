[English](README.md) · [中文](README_cn.md)

# Durweg workflows

**The public list of [Durweg](https://github.com/musetee/durweg) workflows: ready-made ways of
working that you install by name and run with your AI agent.**

## 🧭 Install one

With Durweg installed, tell your agent "Show me the durweg workflows I can install", or run:

1. `durweg library available` to see this list;
2. `durweg library add <name>` (for example `durweg library add human-readme`);
3. tell your agent: "Run <name> with durweg."

## 📚 The workflows

| Name | What it does | Repository |
| :--- | :--- | :--- |
| `human-readme` | AI agents write a project's README in 7 fixed steps, for a first-time reader | [musetee/durweg-human-readme](https://github.com/musetee/durweg-human-readme) |
| `stepaper` | An AI agent reads a research paper with you one step at a time, lets you question every step, then builds the group-meeting slides | [musetee/durweg-stepaper](https://github.com/musetee/durweg-stepaper) |

## 🙋 Add yours

Publish your workflow as a public repository with a LICENSE and say yes when Durweg asks whether
to propose it to the public catalog ([publishing](https://github.com/musetee/durweg/blob/main/docs/publish.md)).
That opens a pull request here. A check makes sure the repository is public, has a README and a
LICENSE and a valid `workflow.json`; the entry is listed once the owner merges it.
