const qualificationBox = document.getElementById("qualificationBox");
const skillsBox = document.getElementById("skillsBox");
const experiencesBox = document.getElementById("experiencesBox");
const projectsBox = document.getElementById("projectsBox");
const experienceItems = document.querySelectorAll(".hidden");
var executed = false; // used solely to ensure an animation plays only once

function hideAll() { // hide all content in mainContent div box
    qualificationBox.style.display="none";
    skillsBox.style.display="none";
    experiencesBox.style.display="none";
    projectsBox.style.display="none";
    scroll(0,0); // goes to the top of the webpage
}

function goHome() {
    hideAll();
    qualificationBox.style.display = "block";
    document.getElementById("pageTitle").innerHTML="SUMMARY OF QUALIFICATIONS";
}

function goSkills() {
    hideAll();
    skillsBox.style.display = "block";
    document.getElementById("pageTitle").innerHTML="SKILLS & EDUCATION";
    eduImage = document.getElementById("eduLogo");
    eduText = document.getElementsByClassName("hiddenCascade")[0];

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting)
            {
                eduText.classList.add("showCascade");
                eduImage.style = "opacity: 0.4";
            }
            else
            {
                eduText.classList.remove("showCascade");
                eduImage.style = "opacity: 1";
            }
        })
    },
    {
        threshold: 1.0
    });

    observer.observe(document.querySelectorAll(".imgCascade")[0]);
}

function goExperiences() {
    hideAll();
    experiencesBox.style.display = "block";
    document.getElementById("pageTitle").innerHTML="EXPERIENCES";

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            entry.target.classList.toggle("show", entry.isIntersecting); // add class "show" when the entry is intersecting, once the isIntersecting is set to false, toggle can only remove "show"
        })
    }, 
    {
        threshold: 0.5 // an additional option: an element is considered to be visible, only when half the element is in the viewport of the intersection observer (THIS INCLUDES IF THE ELEMENT IS HORIZONTALLY SHIFTED!)
    });

    experienceItems.forEach((item) => {
        observer.observe(item)
    })
}

function goProjects() {
    hideAll();
    projectsBox.style.display = "block";
    document.getElementById("pageTitle").innerHTML="PROJECTS";
}