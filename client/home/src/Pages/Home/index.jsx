import React from "react";

export default ({ profile = {} }) => {
    return  `Hi ${profile.name}`
}