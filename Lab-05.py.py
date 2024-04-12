

# CS-500L/Lab-05
# 20099_Md_Maniruzzaman_Lab-05
'''===================================================================================='''


from typing import Optional

class Person:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    def __str__(self) -> str:
        return f"name = {self._name}"
    
    def display(self) -> None:
        print(self)

    def dowork(self) -> None:
        pass

class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self._skills = skills
        self._salary = salary

    def __str__(self) -> str:
        return f"{super().__str__()}\nskills = {self._skills}\nsalary = {self._salary}"
    
    def get_annual_income(self) -> float:
        return self._salary * 12
    
    def dowork(self) -> None:
        print(f"Programmer {self.name} is writing a program.")

class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self._bonus = bonus

    def __str__(self) -> str:
        return f"{super().__str__()}\nbonus = {self._bonus}"
    
    def get_annual_income(self) -> float:
        return super().get_annual_income() + self._bonus
    
    def dowork(self) -> None:
        print(f"Manager {self.name} is supervising a team of programmers.")

class Project:
    def __init__(self, projname: str, budget: float, active: bool) -> None:
        self._projname = projname
        self._budget = budget
        self._active = active

    @property
    def budget(self) -> float:
        return self._budget

    @property
    def active(self) -> bool:
        return self._active

    def __str__(self) -> str:
        return f"projname = {self._projname}\nbudget = {self._budget}\nactive = {self._active}"
    
    def display(self) -> None:
        print(self)

class Group:
    def __init__(self, groupname: str) -> None:
        self._groupname = groupname
        self._members = []

    def add_member(self, member: Programmer) -> None:
        if member not in self._members:
            self._members.append(member)

    def display(self) -> None:
        print("The group has these members:")
        for member in self._members:
            print(f"{member}\n")

    def remove_member(self, name: str) -> None:
        self._members = [member for member in self._members if member.name != name]

    def ask_anyone_dowork(self) -> None:
        for member in self._members:
            member.dowork()

class ITGroup(Group):
    def __init__(self, groupname: str) -> None:
        super().__init__(groupname)
        self._projects = []

    def add_project(self, project: Project) -> None:
        self._projects.append(project)

    def find_largest_project(self):
        def project_budget(proj):
            return proj.budget
    
        return max(self._projects, key=project_budget, default=None)

    def get_active_projects(self) -> list:
        return [project for project in self._projects if project.active]

    def display(self) -> None:
        super().display()
        print("The group has these projects:")
        for project in self._projects:
            print(f"{project}\n")

    def get_allMembers_morethan(self, income: float) -> list:
        return [member for member in self._members if member.get_annual_income() >= income]

    def ask_manager_dowork(self) -> None:
        for member in self._members:
            if isinstance(member, Manager):
                member.dowork()

def main() -> None:
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)
 
    itgrp:ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()
    
    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)
    
    itgrp.ask_anyone_dowork()
    print() 
    itgrp.ask_manager_dowork()
    
    print("\nGet the largest project...")
    maxProj: Optional[Project] = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()
 
    print("\nGet the active projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
        print()
    
 
    itgrp.display()
    itgrp.remove_member(p3.name) 
 
    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
    for member in members:
        member.display()
        print()
 
 
if __name__ == "__main__":
 main()
