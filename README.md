日本語はこちら → [README_ja.md](README_ja.md)
# Honmaru ~ We are currently working diligently ~
This framework worm "Honmaru" aims at Serverless Framework for SAM (*).

(*) [Serverless Application Model](https://github.com/awslabs/serverless-application-model)

## Work schedule
- [x] design
  - [x] To harden what you want to do
  - [x] Make a command system
  - [x] Make a milestone
- [ ] Prior verification
  - [ ] ~~```aws cloudformation package``` Understand what you do with~~
  - [x] Find out how to use Travis CI
  - [x] Selection of framework for CLI Tool in Python 3 system (use click)
  - [ ] Find out how to publish modules in Python
  - [x] Whether it is possible to specify RequestId (?) when executing changeset (enable)
- [ ] Implementation
  - [ ] Create priorities of configuration files, environment variables, command arguments and implement load mechanism
  - [ ] package implementation
  - [ ] Implementing deploy / remove
  - [ ] Implementation of the parameter function
  - [ ] changeset related functions
    - [ ] Implementation of an option that creates only changesets with the deploy command and does not execute it
    - [ ] Implementation of the list-changeset command
    - [ ] Implementation of exec-changeset command
  - [ ] Implementation of module installation
  - [ ] Implement the option to use Docker during module installation
- [ ] Next verification
  - [ ] ```aws cloudformation package``` Understand what you do with
