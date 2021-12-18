import React, { useState, useEffect, useContext } from "react";
import { Context } from "../store/appContext";
import { Redirect } from "react-router-dom";
import default_user from "../../img/profile/default_user.png";
import home from "../../img/profile/home_transparent.png";
import "../../styles/pages/dashboard.scss";
import { DashboardAccount } from "../component/dashboard/dashboardAccount";

export const Dashboard = () => {
	const { actions, store } = useContext(Context);
	let [content, setContent] = useState(null);

	useEffect(
		() => {
			if (store.user.name)
				setContent(
					<div
						className="center"
						style={{ flexDirection: "column", gap: "1.3rem", marginInline: "auto", color: "lightgray" }}>
						<h2>¡Hola {store.user.name.charAt(0).toUpperCase() + store.user.name.slice(1)}!</h2>
						<img src={home} width="100" height="100" style={{ filter: "opacity(15%)" }} />
					</div>
				);
		},
		[store.user.name]
	);

	return !store.user.token ? (
		<Redirect to="/" />
	) : (
		<div className="profile-wrapper">
			<aside className="profile-aside">
				<div className="profile-user-info">
					<div className="profile-img-wrapper">
						<img className="profile-img" src={store.user.img_url || default_user} />
					</div>
					<div className="profile-info">
						<h1 className="profile-username">
							{store.user.name.charAt(0).toUpperCase() +
								store.user.name.slice(1) +
								" " +
								store.user.lastname.charAt(0).toUpperCase() +
								store.user.lastname.slice(1)}
						</h1>
						<p>695 565 910</p>
					</div>
				</div>
				<nav>
					<ul>
						<li>
							<button>Citas</button>
						</li>
						<li>
							<button onClick={() => setContent(<DashboardAccount />)}>Cuenta & Configuración</button>
						</li>
						<li>
							<button className="logout" onClick={() => actions.logout()}>
								Salir
							</button>
						</li>
					</ul>
				</nav>
			</aside>
			<div className="profile-content">{content}</div>
		</div>
	);
};
