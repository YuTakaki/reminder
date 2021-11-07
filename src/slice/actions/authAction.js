import { createAsyncThunk } from "@reduxjs/toolkit";
import axios from "axios";

export const checkAuthenticatedAction = createAsyncThunk(
	"auth/checkAuthenticatedAction",
	async () => {
		const tokens = JSON.parse(localStorage.getItem("reminder"));
		//check for token if exist
		if (!tokens) {
			return { error: "not log in yet", isActive: false };
		}
		try {
			const checkAction = await axios.get("/auth", {
				headers: {
					Authorization: `Bearer ${tokens.access_token}`,
				},
			});
			return {
				isActive: true,
				token: tokens.access_token,
				user: checkAction.data.user,
			};
		} catch (error) {
			return { error: error.response.data, isActive: false };
		}
	}
);

export const signInAction = createAsyncThunk(
	"auth/signInAction",
	async (signInForm) => {
		try {
			const action = await axios.post("/auth/login", signInForm);
			const token = action.data.token;
			localStorage.setItem("reminder", JSON.stringify(token));
			return {
				isActive: true,
				token: token.access_token,
				user: action.data.user,
			};
		} catch (error) {
			return { error: error.response.data, isActive: false };
		}
	}
);
