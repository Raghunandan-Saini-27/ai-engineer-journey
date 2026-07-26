console.log("Javascript Connected Successfully!");

const button = document.getElementById("search-btn");

const DEFAULT_BUTTON_TEXT="Search";

const SEARCHING_BUTTON_TEXT = "Searching...";

const searchBox = document.getElementById("search-box");

const results=document.getElementById("results");

button.addEventListener("click",function()
{
	console.log(searchBox.value);
	searchJobs();
});

searchBox.addEventListener("keydown",function(event)
{
	if(event.key==="Enter")
	{
		event.preventDefault();
		searchJobs();
	}
});

function cleanSearchQuery(search_value)					//Cleans the query
{
	search_value=search_value.trim().toLowerCase();

	return search_value;
}

async function searchJobs()								//Main Controller
{
	const rawQuery=searchBox.value;

	const cleanQuery=cleanSearchQuery(rawQuery);

	if(cleanQuery==="")
	{
		return showMessage("Please enter a valid query.")
	}

	button.disabled=true;

	button.textContent=SEARCHING_BUTTON_TEXT

	showMessage("Searching...");
	
	try{
		const jobs=await fetchJobs(cleanQuery);

		renderJobs(jobs);
	}
	catch(error)
	{
		console.error(error)

		showMessage("Couldn't connect to the server.")
	}
	finally
	{
		button.disabled=false;

		button.textContent=DEFAULT_BUTTON_TEXT;
	}
}

function showMessage(message)					//Displays Messages
{
	results.innerHTML=`<p class=message>${message}<p>`;
}

function createJobCard(job)						//Creates JobCard
{
	const card=document.createElement("div");

	card.className="job-card";

	const subcard=document.createElement("div");

	subcard.className="job-header";

	const job_title=document.createElement("h3");

	const apply_button=document.createElement("button");

	apply_button.addEventListener("click",function()
		{
			window.open(job.link, "_blank")
		}
	)

	const job_company=document.createElement("p");

	const job_location=document.createElement("p");

	const job_description=document.createElement("p");

	job_title.textContent=job.title;

	apply_button.textContent="Apply";

	job_company.textContent=job.company;

	job_location.textContent=job.location;

	job_description.textContent=job.description;

	subcard.appendChild(job_title);

	subcard.appendChild(apply_button);

	card.appendChild(subcard);

	card.appendChild(job_company);

	card.appendChild(job_location);

	card.appendChild(job_description);

	return card;
}

async function fetchJobs(query)					//Fetches job from the backend
{
	const url=`http://127.0.0.1:8000/jobs/smart-search?query=${query}`;
	
	const response=await fetch(url);

	if(!response.ok)
		{
			throw new Error(`HTTP ${response.status}`);
		}

	const jobs=await response.json();	

	return jobs;
}

function renderJobs(jobs)						//Renders the job for displaying on webpage
{
	results.innerHTML = "";

		if(jobs.length===0)
		{
			showMessage("No Results found! Try another keyword.")
		}

		else{
	
		for (const job of jobs)
		{
			const jobCard=createJobCard(job);

			results.appendChild(jobCard);
		}
		}
}