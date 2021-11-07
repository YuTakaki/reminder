import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./slice/authSlicer";

export const store = configureStore({
	reducer: {
		auth: authReducer,
	},
});
