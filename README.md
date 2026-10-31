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
| `write-your-method` | Comes with Durweg, nothing to install: write down your own way of working as a workflow. Tell your agent: "Run write-your-method with durweg." | [musetee/durweg](https://github.com/musetee/durweg#-example-write-down-your-method) |
| `human-readme` | AI agents write a project's README in 7 fixed steps, for a first-time reader | [musetee/durweg-human-readme](https://github.com/musetee/durweg-human-readme) |
| `name-project` | Find a name for a project: core value, white space, candidates, a collision check, one decision | [musetee/name-project](https://github.com/musetee/name-project) |

## 🙋 Add yours

Publish your workflow as a public repository with a LICENSE and say yes when Durweg asks whether
to propose it to the public catalog ([publishing](https://github.com/musetee/durweg/blob/main/docs/publish.md)).
That opens a pull request here. A check makes sure the repository is public, has a README and a
LICENSE and a valid `workflow.json`; the entry is listed once the owner merges it.
