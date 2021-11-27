import React, { useContext } from "react";
import { Context } from "../../store/appContext";
import PropTypes from "prop-types";
import "../../../styles/components/calendar.scss";
import { Link } from "react-router-dom";

export const Day = props => {
	const { store, actions } = useContext(Context);
	return (
		<>
			{props.isOnClickDay !== undefined ? (
				<button
					className={"center day" + (props.isLight ? " light-color-day" : "")}
					onClick={() => actions.calendarActions.updateCalendar(props.isOnClickDay)}>
					{props.date.getDate()}
				</button>
			) : (
				<Link
					to="/"
					className={
						"center day" + (props.isLight ? " light-color-day" : "") + (props.isToday ? " today" : "")
					}>
					{props.date.getDate()}
				</Link>
			)}
		</>
	);
};

Day.propTypes = {
	date: PropTypes.object,
	isLight: PropTypes.bool,
	isToday: PropTypes.bool,
	isOnClickDay: PropTypes.bool
};
