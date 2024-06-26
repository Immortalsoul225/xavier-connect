const SubEventCard = (props) => {
  return (
    <div class="card border-success col-12 col-md-5 col-lg-4 mb-3 card-margin">
      <img src={props.img} class="card-img-top" alt="Reel" />
      <div class="card-body d-flex flex-column justify-content-between">
        <div>
          <h5 class="card-title event-font">{props.name}</h5>
          <p class="card-text description-font">{props.desc}</p>
        </div>

        <div>
          <h6 class="event-font">Contact Student Coordinator</h6>
          {props.cord.map((item) => (
            <p class="description-font">
              <strong>{item.name}</strong>
              <span
                class="text-primary"
                style={{ textDecoration: "underline", marginLeft: "20px" }}
              >
                {item.contact_no}
              </span>
            </p>
          ))}

          <details className="description-font" id="details1">
            <summary>Read More</summary>
            <div dangerouslySetInnerHTML={{ __html: props.rules }} />
          </details>
        </div>
      </div>
    </div>
  );
};

export default SubEventCard;
