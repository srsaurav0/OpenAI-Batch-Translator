def get_text_lists():
    # Multiple lists of strings to translate
    texts_list_1 = get_tpls_5()

    # texts_list_2 = get_tpls_5()

    # texts_list_3 = get_tpls_6()

    texts_lists = [texts_list_1]

    return texts_lists

def get_inis():
    inis = [
        """RentByOwner.com offers a comprehensive online platform for travelers seeking the perfect vacation rental experience. With a wide selection of properties ranging from cozy holiday homes to luxurious villas, we cater to diverse travel needs and budgets. Our user-friendly website provides detailed property descriptions, photos, reviews, and easy booking options, ensuring a seamless rental process. RentByOwner.com aggregates over 10M properties from many travel sellers to give you a diverse selection of vacation homes to choose to create better travel memories.""",
        """<p> At Rent By Owner, we want everyone to be an owner, just as we want everyone to be a traveler. In creating more travelers, hopefully we are creating more owners. And in creating more owners, we will be creating more travelers. You can <a class="static-page-link" target="_blank" rel="noopener noreferrer" href="https://www.upnextgroup.com/about-us">read more about our core values</a> for UpNext Group here. We also look forward to showing you what we are creating in the months and years ahead. Stay tuned.</p>""",
        """<p> Historically, Rent By Owner has been a meta brand, connecting travelers to travel sellers, and since 2013, this has served us well. We believe that by helping more than a million travelers, we now have a great base on which to build something new and spectacular. Going forward, we need to build closer relationships with both sides of the market--both travelers and owners-- so as to bring them together in new ways and into a deeper relationship with each other and the communities into which the traveler journeys.</p>""",
        """<p> At Rent By Owner, we are focusing on the Alternative Accommodations market. We believe this market encourages people to have a more authentic travel experience in the communities, homes, and places of others. Creating a direct connection between a traveler and an owner creates a more meaningful experience. Sharing cultures, recipes, local tips, insights, pride, activities, art, food, entertainment... sights, sounds, smells and senses. These are the memories worth sharing.</p>""",
        """<p> We believe life is better when you venture out and explore the world. You meet other people, you connect with family & friends, you do more business, and you have new experiences. In short, travel creates memories. Travel brings people closer together and fosters better understanding of each other and ourselves.</p>""",
        """<p> Rent By Owner relies on the eco-score created by <a class="static-page-link" target="_blank" rel="noopener noreferrer" href="https://www.onedegreeleft.com">One Degree Left</a>, a sister-company operated by parent company UpNext Group. This property looks at a number of factors to help score all properties based on a variety of sustainability factors. We believe that we can help elevate properties that have good environmental and sustainability practices. If we identify a property that has good practices, we will rank that property higher in our search results than other properties. By ranking these properties higher, hopefully they will be booked with greater frequency and nudge behavior by a small factor… by ‘one degree’ if you will. While it is not perfect, it is part of our commitment to driving more sustainable travel.</p>"""
    ]
    return inis

def get_tpls():
    tpls = [
"""{{template "common/redirect/redirect.tpl" .}}

{{define "site_common_preload"}}
    <link rel="preload" href="{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2" as="font" type="font/woff2" crossorigin>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css" as="style"/>
{{end}}

{{define "site_header_logo_redirect"}}
    <a href="/" class="align-item-center">
        <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26">
    </a>
{{end}}

{{define "site_redirect_container_logo"}}
    <div class="box logo-area">
        <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26" />
    </div>
{{end}}""",
"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/details/published_details.tpl" .}}

{{define  "site_css_vars"}}
    <style>
        :root {
            /* Site 'Details' css image variable start*/
            --site-common-details-bottom-links-bullet: url({{.staticFileUrl}}/static/images/sites/rentbyowner.com/check.svg);
        }
    </style>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"
          as="style"/>
{{end}}

{{define "site_details_popup_header"}}
    <img class="max-w-full nav-row-logo" loading="lazy"
         src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}"
         width="182"
         height="26">
{{end}}

{{define "details_breadcrumb"}}
    {{template "common/details/partials/details_breadcrumb.tpl" .}}
{{end}}

{{define "map_area_description"}}
    {{template "common/details/partials/details_area_description_map.tpl" .}}
{{end}}

{{define "seo_room_arragment_faq"}}
    {{template "common/details/partials/details_seo_room_arragment_faq.tpl" .}}
{{end}}

{{define "map"}}
    {{template "common/details/partials/details_map.tpl" .}}
{{end}}

{{define "details_faq"}}
    {{template "common/details/partials/faq.tpl" .}}
{{end}}

{{define "details_mobile_review"}}
    {{template "common/details/partials/details_mobile_reviews.tpl" .}}
{{end}}

<!-- Bedroom footer content start -->
{{define "site_bedroom_footer_content"}}
    <div class="bedroom-footer-content">
        <div class="bedroom-footer text-white" id="js-seo-block">
            <div class="max-container">
                <div class="container-fluid">
                    <h3 class="bedroom-footer-title font-20 no-margin pb-16 underlined-title">
                        Why is Rent By Owner {{.LocationName}} Your Choice for Vacation Rentals
                    </h3>
                    <div class="color-accent">
                        <p>Find your dream vacation rental on Rent By Owner, where
                            adventure meets comfort in every corner. RentByOwner features a broad mix of accommodations,
                            from charming country cottages and chic city apartments to tranquil beachfront villas and
                            cozy mountain cabins. Whether you're yearning for a delightful bungalow by the bay, a grand
                            estate over the dock, or a snug lodge in a quaint village, we've got the perfect spot for
                            you.</p>
                        <div class="{{if eq .UserInfo.Platform "mobile"}}hidden{{else}}visible{{end}}" id="js-seo-text-section">
                            <p>Prepare to unleash your inner explorer with our unique lodgings, including floating
                                houses, whimsical treehouses, and picturesque farmhouses, or stick to the classics with
                                duplexes, flats, and guesthouses. Choose the simplicity of a studio or the luxury of a
                                suite. For outdoor enthusiasts, we offer tents in hidden campsites, RVs, mountain
                                cabins, boat rentals, chalets in snowy havens, and caravans in lush gardens. Rent By
                                Owner truly has something for everyone.</p>
                            <p>Every holiday rental, from a humble hut to a lavish resort, guarantees a memorable stay
                                with cozy beds, functional kitchens, and welcoming living areas. Ideal for families,
                                couples, or solo adventurers, our rentals are more than just a place to sleep—they're
                                your home away from home. Book your next vacation with us and embark on a unique retreat
                                crafted for relaxation and adventure. We also offer annexes for added privacy, designer
                                lofts for a modern touch, and motels for quick stays. Explore beachside bungalows,
                                countryside ranches, and urban condos. Find your perfect getaway, whether it’s a quiet
                                den in the forest or a bustling inn by the island. At RentByOwner, our properties
                                include everything from houseboats and barns to court-style quarters and garden
                                retreats.</p>
                            <p>To make your booking experience even more convenient, we help you compare prices and
                                inventory so you can find and book your vacation rental on popular platforms like
                                Airbnb, Expedia, Vrbo (previously HomeAway), TripAdvisor (FlipKey), Booking.com, and
                                HomeToGo. We work with these trusted sites to offer you a seamless booking process,
                                ensuring that your perfect vacation rental is just a few clicks away.</p>
                        </div>
                    </div>
                    <div class="read-more-less {{if eq .UserInfo.Platform "mobile"}}visible{{else}}hidden{{end}}">
                        <div class="read-more cursor-pointer" id="js-seo-read-more">
                            <span class="text-white">{{i18n .Lang "__show_more"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                        <div class="read-less read-more-container cursor-pointer hidden" id="js-seo-read-less">
                            <span class="text-white">{{i18n .Lang "show_less"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{{end}}
<!-- Bedroom footer content start -->
""",
"""{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/faq_container.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/sub_location.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/faq_container.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/sub_location.css" as="style"/>
{{end}}""",
"""<p>There are <span>{{if .PrivatePoolCount}}{{.PrivatePoolCount}}{{end}}</span> vacation rentals with private pools near <span>{{.LocationName}}</span>. Top-rated RBO homes that have access to a swimming pool include:</p>""",
"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/listing/refine.tpl" .}}
{{template "common/partials/blank_bookmark_mobile.tpl" .}}

{{define  "site_css_vars"}}
    <style>
        :root {
            /* Site 'Category' css image variable start*/
            --site-common-listing-bottom-links-bullet: url({{.staticFileUrl}}/static/images/sites/rentbyowner.com/check.svg);
        }
    </style>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/category.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/category.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/refine.css" as="style"/>

{{end}}""",
"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/listing/complex_list.tpl" .}}

{{define "site_css"}}
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
<link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
{{end}}

{{define "site_preload"}}
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css" as="style"/>
<link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css" as="style"/>
{{end}}
"""
    ]
    return tpls


def get_complex_sentences():
    sentences = [
        "Although the weather forecast predicted rain, we decided to go hiking, hoping the storm would pass quickly.",
        "The scientist, who had spent years studying marine life, discovered a new species of fish while conducting an expedition in the deep sea.",
        "After finishing her final exams, Sarah, exhausted but relieved, treated herself to a long weekend getaway with her friends.",
        "Despite the challenges of learning a new language, many students find that their ability to communicate improves rapidly with consistent practice.",
        "The book, which was recommended by my teacher, provided fascinating insights into the complexities of human behavior and decision-making.",
        "As the sun began to set, the sky turned a brilliant shade of pink, and we stood in awe, enjoying the quiet beauty of nature.",
        "While she was preparing dinner, her phone rang with an unexpected call, but she chose to ignore it in favor of finishing her task.",
        "The company, after years of growth and expansion, faced significant financial setbacks due to unforeseen market shifts and internal mismanagement.",
        "Although he was initially skeptical of the new technology, he soon realized its potential after attending the demonstration, which showcased its impressive capabilities.",
        "The concert, held in the heart of the city, attracted a diverse crowd, and the energy in the air was palpable as the band took the stage."
    ]
    return sentences

def get_tpls_2():
    tpls = [
"""<p>If you're looking for a unique vacation rental in {{.LocationName}}, we've got just the thing.
    RVs, boats and tree houses are all available through our platform. We have a wide variety of properties
    to choose from, so you can find the perfect one for your needs. Our vacation rentals are affordable and
    come with all the amenities you need for a comfortable stay.
</p>""",
"""{{if eq .pageLayout "SubLocation:Hotel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/hotels.tpl" .}}
{{else if eq .pageLayout "SubLocation:VacationRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:Cottage"}}
    {{template "sites/rentbyowner.com/sub_page/lang/cottages.tpl" .}}
{{else if eq .pageLayout "SubLocation:Cabin"}}
    {{template "sites/rentbyowner.com/sub_page/lang/cabins.tpl" .}}
{{else if eq .pageLayout "SubLocation:Villa"}}
    {{template "sites/rentbyowner.com/sub_page/lang/villas.tpl" .}}
{{else if eq .pageLayout "SubLocation:Resort"}}
    {{template "sites/rentbyowner.com/sub_page/lang/resorts.tpl" .}}
{{else if eq .pageLayout "SubLocation:FamilyRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/family_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:PetFriendly"}}
    {{template "sites/rentbyowner.com/sub_page/lang/pet_friendly.tpl" .}}
{{else if eq .pageLayout "SubLocation:Pool"}}
    {{template "sites/rentbyowner.com/sub_page/lang/rentals_with_pools.tpl" .}}
{{else if eq .pageLayout "SubLocation:Oceanfront"}}
    {{template "sites/rentbyowner.com/sub_page/lang/oceanfront.tpl" .}}
{{else if eq .pageLayout "SubLocation:Beach"}}
    {{template "sites/rentbyowner.com/sub_page/lang/beach_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:LuxuryRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/luxury_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:DiscountRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/discount_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:BusinessTravel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/business_travel.tpl" .}}
{{else if eq .pageLayout "SubLocation:ShortTermStay"}}
    {{template "sites/rentbyowner.com/sub_page/lang/short_term_stays.tpl" .}}
{{else if eq .pageLayout "SubLocation:SustainableTravel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/sustainable_travel.tpl" .}}
{{else if eq .pageLayout "SubLocation:SkiChalet"}}
    {{template "sites/rentbyowner.com/sub_page/lang/ski_chalets.tpl" .}}
{{else if eq .pageLayout "SubLocation:Timeshare"}}
    {{template "sites/rentbyowner.com/sub_page/lang/timeshares.tpl" .}}
{{else if eq .pageLayout "SubLocation:GroupTravel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/group_travel.tpl" .}}
{{else if eq .pageLayout "SubLocation:WinterRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/winter_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:SummerRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/summer_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:MonthlyStay"}}
    {{template "sites/rentbyowner.com/sub_page/lang/monthly_stays.tpl" .}}
{{else if eq .pageLayout "SubLocation:HolidayHomes"}}
    {{template "sites/rentbyowner.com/sub_page/lang/holiday_homes.tpl" .}}
{{else if eq .pageLayout "SubLocation:UniqueVacationRentals"}}
    {{template "sites/rentbyowner.com/sub_page/lang/unique_vacation_rentals.tpl" .}}
{{else}}
    {{template "sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl" .}}
{{end}}""",
"""<p>
    Looking for a beach rental rent near {{.LocationName}}? Rent By Owner features {{if gt .Count 1}}more than {{.Count}}{{end}} beach
    rentals that are perfect for your next beach holiday. Discover luxury beach rentals that are
    within walking distance away from {{.LocationName}}. Several of these vacation rentals in {{.LocationName}}
    are kid-friendly & family-friendly, and are near top local attraction spots, to give guests an
    unforgettable travel experience. RBO’s rental listings come in all shapes and sizes for large
    groups, friends, or couples, or wedding retreats in {{.LocationName}}.
</p>
<p>
    Rent By Owner Offers  {{if gt .Count 1}}{{.Count}}{{end}} holiday homes and places to stay in {{.LocationName}}. The site provides
    unique Airbnb, VRBO, RBO-style accommodations to fit your trip or get away with your friends and family.
</p>
<p>
    RBO beachfront rentals give you the best travel experience that makes it easy to find and book
    the best place to stay at the best destinations.
</p>""",
"""<p>
    Discover {{if gt .Count 0}}more than {{.Count}}{{else}}the best{{end}} vacation rentals in {{.LocationName}} that are perfect for your next trip.
    Whether you are traveling with a group, family, friends, or couples retreat in {{.LocationName}},
    RBO has all types of rental properties with top amenities, including indoor/outdoor/private
    swimming pools, Wi-Fi, hot tubs, self-catering, and more.
</p>
<p>
    Rent By Owner offers vacation rentals near {{.LocationName}} for all types of travelers,
    whether you are looking for a luxury home, villa, resort, condo, cabin, cottage, RV rental,
    or <a href="{{.UrlPrefix}}{{.LocationSlug}}/{{i18n .Lang "__pet_friendly_rentals"}}" class="static-page-link">pet friendly accommodation in {{.LocationName}}</a>.
    Rent By Owner makes it easy to find and compare vacation rentals, matching you with rental
    properties from different vacation rental websites. By comparing these rental properties,
    RBO helps you find the best deals in {{.LocationName}}.{{if and (.StartAtPrice) (gt .StartAtPrice 0.0) (gt .Count 0)}}<a href="{{.UrlPrefix}}{{.LocationSlug}}/{{i18n .Lang "__luxury_rentals"}}" class="static-page-link">
    Luxury vacation rental</a> prices start from <span id="js-start-price-1">{{.UserCurrency.Symbol}}{{UserPrice .StartAtPrice .UserCurrency.Rate}}</span>
    per night and affordable condos in {{.LocationName}} start from <span id="js-start-price-2">{{.UserCurrency.Symbol}}{{UserPrice .StartAtPrice .UserCurrency.Rate}}</span> per night.{{end}}
</p>
<p>
    RBO offers a large selection of vacation rentals from top leading sites such as Booking.com,
    Airbnb, VRBO, Trip.com, RV Share, Outdoorsy, and many more providers. Filter your search
    dates and discover {{.LocationName}} vacation homes for your next trip.
</p>""",
"""<p>
    {{if gt .Count 1}}With more than {{.Count}}{{else}}Rent By Owner features{{end}} sustainable places to stay in {{.LocationName}}, and with a range of
    eco-friendly vacation rentals for your sustainable travel, Rent By Owner can help its users
    make good travel decisions. Whether you are looking for weekly/monthly vacation homes, cabins,
    villas, cottages, eco-hostels, or luxurious boutique hotels in {{.LocationName}}, there’s definitely
    something for you.
</p>
<p>
    Rent By Owner offers {{if gt .Count 0}}{{.Count}}{{end}} eco-friendly accommodations with a variety offer price ranges,
    styles, and top amenities. Some of these amenities include solar heating, greenwater collection,
    natural gardens, smart thermostats, sustainable furnishings, and more. RBO has covered a wide
    range of locations, no matter where you are visiting, RBO would make it easy to find and navigate
    the perfect eco-friendly place to stay that is within your budget.
</p>
<p>
    RBO lists properties as scored by its sister company, <a target="_blank" href="https://www.onedegreeleft.com">OneDegreeLeft</a>, from most- to least
    eco-friendly. While not every property. We believe that together we can make travel better.
    Explore eco-friendly travel with family, friends, or colleagues. RBO will try to help ensure
    your next trip to  {{.LocationName}} is enjoyable and safe for you and the environment. book an
    eco-friendly place to stay with RBO today!
</p>"""
    ]
    return tpls

def get_tpls_3():
    tpls = [
"""<p>
    {{.LocationName}} is a family-friendly destination with {{if gt .Count 1}}more than {{.Count}}{{else}}top{{end}} places to stay. {{.LocationName}}
    timeshare rental offers luxury vacation homes while providing comfort for large groups or the
    entire family. It is difficult to strike a balance between having a luxury timeshare rental and
    a cost-effective one when searching for yourself. However, with the aid of Rent By Owner,
    comparing costs, rental locations, available amenities, and closeness to tourist spots in
    {{.LocationName}} can be done with a few simple clicks.
</p>
<p>
    Apart from having kid-friendly entertainment, local food restaurants, and closeness to vacation
    spots, Rent By Owner offers plenty of vacation homes in {{.LocationName}} that are within a short drive
    away. Find your timeshare rental in {{.LocationName}} that includes outdoor pools, hot tubs, dining
    facilities, WiFi, and furnished luxury rooms at your disposal. There are great places you can
    visit in {{.LocationName}} with endless opportunities to explore.
</p>
<p>
    Rent By Owner has a large list of timeshare resorts, condos, ski-in/ski-out chalets, and
    vacation rentals in {{.LocationName}}. Many of these rentals come with fitness centers and playgrounds,
    spacious bedrooms, kitchen facilities, and other amenities that would make your trip an
    unforgettable one. Give yourself a big treat by taking a short trip for adventure. During the
    summer or spring, you will get all timeshare rental in {{.LocationName}} through the RBO website with
    an updated prices for {{.Year}}. Search and book
    <a href="{{.UrlPrefix}}{{.LocationSlug}}/{{i18n .Lang "__vacation_rentals"}}" class="static-page-link">vacation rentals in {{.LocationName}}</a>
    with RBO to reduce
    costs as well as having a stress-free booking from the comfort of your home.
</p>""",
"""<p>
    We have {{if gt .Count 1}}{{.Count}}{{else}}unique style{{end}} family-friendly rentals in {{.LocationName}}. Looking for the best place to stay in
    {{.LocationName}} for your family reunion or retreat?
</p>
<p>
    Rent By Owner offers a variety of options of homes with multiple bedrooms and beds  - perfect
    for large families or groups, and inter-generational travel. Find a place that is good for all
    ages, even if you have a large family with kids, parents, cousins, aunts, uncles, in-laws,
    grandma and grandpa, and even the family pet that'll be coming to {{.LocationName}} with you. RBO
    family rentals have rental properties that would accommodate everyone, saving money vs. a hotel,
    and giving everyone enough space for relaxation. Smaller or single families are not left out,
    there’s something special for everyone.
</p>
<p>
    Renting a {{.LocationName}} family vacation rental on Rent By Owner gives you many options to aid you
    in making the perfect selection for your family holiday. Our {{.LocationName}} house rentals come with
    all the required amenities you need for planning the perfect family vacation; such as
    comfortable beds, TVs, spas, bathtubs, balconies, lawns, playrooms, cribs, Wi-Fi, or swimming
    pools for an unforgettable trip with the entire family and kids.
</p>
<p>
    Rent By Owner offers thousands of rentals.There are many well-equipped cabins,
    villas, family condos, lodges, and more to accommodate large groups or multiple families. Many
    of our holiday rentals also have large private pools and allow you to extend your budget.
</p>""",
"""<p>Ski-chalets are a popular choice in {{.LocationName}}. At Rent By Owner, we offer {{if gt .Count 1}}more than {{.Count}}{{else}}unique{{end}}
    ski chalets near {{.LocationName}} to suit your budget and preferences. These chalets are a great option for those looking for a place
    to stay while enjoying their skiing and snowboarding adventures in the winter, or hiking in the summer.
    Rent By Owner vacation homes are perfect for families, groups, friends, or wedding retreats, and they come
    with great amenities.</p>
<p>
    Rent By Owner offers several luxury chalets to those who love outdoor travel experiences.
    The site provides dog-friendly & self-catering ski chalet rentals near {{.LocationName}}, so you can
    take on all of your adventures with ease, then come back to your rental for more pleasure and comfort.
</p>
<p>
    If you love chalet skiing with patio options or private chalets, there are {{if gt .Count 1}} more than {{.Count}}{{else}}many{{end}}
    of them available near {{.LocationName}}. Some examples of these chalets include romantic chalets,
    mountain chalets, catered ski chalets, and self-catering ski chalets. Your vacation gets better
    as you book your holiday chalet with RBO for your next trip.
</p>

<p>
    Rent By Owner has a large list of Airbnb, VRBO, RBO-style ski chalets, holiday rentals, and
    vacation homes that could be the perfect option for your next trip. Get ready for your next
    getaway by booking a top-rated chalet in {{.LocationName}} with views of the beautiful scenery & the
    best activities to engage with. So whether you are looking for a romantic place for the weekend,
    a spacious chalet for your family or friends, or something for yourself alone, you are one click
    away from getting all these on Rent By Owner.
</p>""",
"""<p>
    Are you looking for a luxury cabin rental in or near {{.LocationName}}? We have plenty of cabin rentals
    in {{.LocationName}} that you can book without any hassle, both during winter & summer season.
    These rentals have luxury bedrooms, as well as other basic amenities to give you optimal comfort.
    Apart from having the best cabins in {{.LocationName}} for rent, there are lots of things you can do near
    {{.LocationName}} that would guarantee you have the best travel experience.
</p>
<p>
    Rent By Owner welcomes travelers from different parts of the world, and in all seasons of the year.
    Rent By Owner ensures you get the best cabin rentals in {{.LocationName}}. Cabins make for a great accommodation
    option when traveling with family, friends, and large groups, especially in {{.LocationName}}{{ if .GeoInfo.StateAbbr }}, {{.GeoInfo.StateAbbr}}{{ end }}.
</p>
<p>
    Users have the flexibility of comparing {{if gt .Count 1}}{{.Count}}{{end}} beautiful rental cabins in {{.LocationName}} with Rent By Owner.
    You are just a few clicks away from enjoying large cabins, lakefront cabins, pet-friendly cabins,
    ski cabins, or a family cabin rental getaway. RBO's large selection of cabins for rent in {{.LocationName}},
    will ensure we have something right for you.
</p>""",
"""<p>
    Visiting {{.LocationName}} and looking for accommodation? A vacation condo rental is perfect
    for those visiting and need more flexibility than a hotel. {{if gt .Count 0}}With more than {{.Count}}{{else}}Discover{{end}} condo rentals
    and holiday apartments in {{.LocationName}} listed on Rent By Owner, we can help you find the best place to stay.
</p>
<p>
    Many of the best vacation  condos in {{.LocationName}} come with top amenities, including
    swimming pools, fitness centers, Wi-Fi, luxury suites, fully-equipped kitchens, and more.
    Whatever your budget is, there’s likely a condo that would fit it. Now you can start preparing
    for your next trip to {{.LocationName}} and book your accommodation in minutes on our website.
</p>
<p>
    RBO vacation condo rentals are the best place for guests to start creating an unforgettable
    travel experience. Vacation condos are perfect for romantic getaways and weekend retreats.
    They give you enough space, well-equipped kitchens, and more room to make it feel like home.
    You can book a place to stay in {{.LocationName}} right now with Rent By Owner and have a whole list
    of condos to choose from.
</p>
<p>
    Book for a short-stay or long-stay condo for any of your favorite travel destinations.
    Compare condos, apartments, townhomes, villas and more with Rent By Owner.
</p>"""
    ]
    return tpls

def get_tpls_4():
    tpls = {
"key_1":"""<p>If you're looking for a unique vacation rental in {{.LocationName}}, we've got just the thing.
    RVs, boats and tree houses are all available through our platform. We have a wide variety of properties
    to choose from, so you can find the perfect one for your needs. Our vacation rentals are affordable and
    come with all the amenities you need for a comfortable stay.
</p>""",
"key_2":"""{{if eq .pageLayout "SubLocation:Hotel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/hotels.tpl" .}}
{{else if eq .pageLayout "SubLocation:VacationRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:Cottage"}}
    {{template "sites/rentbyowner.com/sub_page/lang/cottages.tpl" .}}
{{else if eq .pageLayout "SubLocation:Cabin"}}
    {{template "sites/rentbyowner.com/sub_page/lang/cabins.tpl" .}}
{{else if eq .pageLayout "SubLocation:Villa"}}
    {{template "sites/rentbyowner.com/sub_page/lang/villas.tpl" .}}
{{else if eq .pageLayout "SubLocation:Resort"}}
    {{template "sites/rentbyowner.com/sub_page/lang/resorts.tpl" .}}
{{else if eq .pageLayout "SubLocation:FamilyRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/family_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:PetFriendly"}}
    {{template "sites/rentbyowner.com/sub_page/lang/pet_friendly.tpl" .}}
{{else if eq .pageLayout "SubLocation:Pool"}}
    {{template "sites/rentbyowner.com/sub_page/lang/rentals_with_pools.tpl" .}}
{{else if eq .pageLayout "SubLocation:Oceanfront"}}
    {{template "sites/rentbyowner.com/sub_page/lang/oceanfront.tpl" .}}
{{else if eq .pageLayout "SubLocation:Beach"}}
    {{template "sites/rentbyowner.com/sub_page/lang/beach_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:LuxuryRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/luxury_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:DiscountRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/discount_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:BusinessTravel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/business_travel.tpl" .}}
{{else if eq .pageLayout "SubLocation:ShortTermStay"}}
    {{template "sites/rentbyowner.com/sub_page/lang/short_term_stays.tpl" .}}
{{else if eq .pageLayout "SubLocation:SustainableTravel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/sustainable_travel.tpl" .}}
{{else if eq .pageLayout "SubLocation:SkiChalet"}}
    {{template "sites/rentbyowner.com/sub_page/lang/ski_chalets.tpl" .}}
{{else if eq .pageLayout "SubLocation:Timeshare"}}
    {{template "sites/rentbyowner.com/sub_page/lang/timeshares.tpl" .}}
{{else if eq .pageLayout "SubLocation:GroupTravel"}}
    {{template "sites/rentbyowner.com/sub_page/lang/group_travel.tpl" .}}
{{else if eq .pageLayout "SubLocation:WinterRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/winter_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:SummerRental"}}
    {{template "sites/rentbyowner.com/sub_page/lang/summer_rentals.tpl" .}}
{{else if eq .pageLayout "SubLocation:MonthlyStay"}}
    {{template "sites/rentbyowner.com/sub_page/lang/monthly_stays.tpl" .}}
{{else if eq .pageLayout "SubLocation:HolidayHomes"}}
    {{template "sites/rentbyowner.com/sub_page/lang/holiday_homes.tpl" .}}
{{else if eq .pageLayout "SubLocation:UniqueVacationRentals"}}
    {{template "sites/rentbyowner.com/sub_page/lang/unique_vacation_rentals.tpl" .}}
{{else}}
    {{template "sites/rentbyowner.com/sub_page/lang/vacation_rentals.tpl" .}}
{{end}}""",
"key_3":"""<p>
    Looking for a beach rental rent near {{.LocationName}}? Rent By Owner features {{if gt .Count 1}}more than {{.Count}}{{end}} beach
    rentals that are perfect for your next beach holiday. Discover luxury beach rentals that are
    within walking distance away from {{.LocationName}}. Several of these vacation rentals in {{.LocationName}}
    are kid-friendly & family-friendly, and are near top local attraction spots, to give guests an
    unforgettable travel experience. RBO’s rental listings come in all shapes and sizes for large
    groups, friends, or couples, or wedding retreats in {{.LocationName}}.
</p>
<p>
    Rent By Owner Offers  {{if gt .Count 1}}{{.Count}}{{end}} holiday homes and places to stay in {{.LocationName}}. The site provides
    unique Airbnb, VRBO, RBO-style accommodations to fit your trip or get away with your friends and family.
</p>
<p>
    RBO beachfront rentals give you the best travel experience that makes it easy to find and book
    the best place to stay at the best destinations.
</p>""",
    }
    return tpls

def get_tpls_5():
    tpls = {
"key_1":"""{{template "common/redirect/redirect.tpl" .}}

{{define "site_common_preload"}}
    <link rel="preload" href="{{.staticFileUrl}}/static/fonts/Muli_Webfont.woff2" as="font" type="font/woff2" crossorigin>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css" as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/redirect.css" as="style"/>
{{end}}

{{define "site_header_logo_redirect"}}
    <a href="/" class="align-item-center">
        <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26">
    </a>
{{end}}

{{define "site_redirect_container_logo"}}
    <div class="box logo-area">
        <img src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/logo_footer.svg" alt="{{i18n .Lang "brand"}}" width="182" height="26" />
    </div>
{{end}}""",
"key_2":"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/details/published_details.tpl" .}}

{{define  "site_css_vars"}}
    <style>
        :root {
            /* Site 'Details' css image variable start*/
            --site-common-details-bottom-links-bullet: url({{.staticFileUrl}}/static/images/sites/rentbyowner.com/check.svg);
        }
    </style>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"
          as="style"/>
{{end}}

{{define "site_details_popup_header"}}
    <img class="max-w-full nav-row-logo" loading="lazy"
         src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}"
         width="182"
         height="26">
{{end}}

{{define "details_breadcrumb"}}
    {{template "common/details/partials/details_breadcrumb.tpl" .}}
{{end}}

{{define "map_area_description"}}
    {{template "common/details/partials/details_area_description_map.tpl" .}}
{{end}}

{{define "seo_room_arragment_faq"}}
    {{template "common/details/partials/details_seo_room_arragment_faq.tpl" .}}
{{end}}

{{define "map"}}
    {{template "common/details/partials/details_map.tpl" .}}
{{end}}

{{define "details_faq"}}
    {{template "common/details/partials/faq.tpl" .}}
{{end}}

{{define "details_mobile_review"}}
    {{template "common/details/partials/details_mobile_reviews.tpl" .}}
{{end}}

<!-- Bedroom footer content start -->
{{define "site_bedroom_footer_content"}}
    <div class="bedroom-footer-content">
        <div class="bedroom-footer text-white" id="js-seo-block">
            <div class="max-container">
                <div class="container-fluid">
                    <h3 class="bedroom-footer-title font-20 no-margin pb-16 underlined-title">
                        Why is Rent By Owner {{.LocationName}} Your Choice for Vacation Rentals
                    </h3>
                    <div class="color-accent">
                        <p>Find your dream vacation rental on Rent By Owner, where
                            adventure meets comfort in every corner. RentByOwner features a broad mix of accommodations,
                            from charming country cottages and chic city apartments to tranquil beachfront villas and
                            cozy mountain cabins. Whether you're yearning for a delightful bungalow by the bay, a grand
                            estate over the dock, or a snug lodge in a quaint village, we've got the perfect spot for
                            you.</p>
                        <div class="{{if eq .UserInfo.Platform "mobile"}}hidden{{else}}visible{{end}}" id="js-seo-text-section">
                            <p>Prepare to unleash your inner explorer with our unique lodgings, including floating
                                houses, whimsical treehouses, and picturesque farmhouses, or stick to the classics with
                                duplexes, flats, and guesthouses. Choose the simplicity of a studio or the luxury of a
                                suite. For outdoor enthusiasts, we offer tents in hidden campsites, RVs, mountain
                                cabins, boat rentals, chalets in snowy havens, and caravans in lush gardens. Rent By
                                Owner truly has something for everyone.</p>
                            <p>Every holiday rental, from a humble hut to a lavish resort, guarantees a memorable stay
                                with cozy beds, functional kitchens, and welcoming living areas. Ideal for families,
                                couples, or solo adventurers, our rentals are more than just a place to sleep—they're
                                your home away from home. Book your next vacation with us and embark on a unique retreat
                                crafted for relaxation and adventure. We also offer annexes for added privacy, designer
                                lofts for a modern touch, and motels for quick stays. Explore beachside bungalows,
                                countryside ranches, and urban condos. Find your perfect getaway, whether it’s a quiet
                                den in the forest or a bustling inn by the island. At RentByOwner, our properties
                                include everything from houseboats and barns to court-style quarters and garden
                                retreats.</p>
                            <p>To make your booking experience even more convenient, we help you compare prices and
                                inventory so you can find and book your vacation rental on popular platforms like
                                Airbnb, Expedia, Vrbo (previously HomeAway), TripAdvisor (FlipKey), Booking.com, and
                                HomeToGo. We work with these trusted sites to offer you a seamless booking process,
                                ensuring that your perfect vacation rental is just a few clicks away.</p>
                        </div>
                    </div>
                    <div class="read-more-less {{if eq .UserInfo.Platform "mobile"}}visible{{else}}hidden{{end}}">
                        <div class="read-more cursor-pointer" id="js-seo-read-more">
                            <span class="text-white">{{i18n .Lang "__show_more"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                        <div class="read-less read-more-container cursor-pointer hidden" id="js-seo-read-less">
                            <span class="text-white">{{i18n .Lang "show_less"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{{end}}
<!-- Bedroom footer content start -->
""",
"key_3":"""{{ if gt .Count 1}}
    <p>With more than {{.LessCount}} {{.LocationName}} vacation rentals, we can help you find a place to stay. These rentals, including vacation rentals, Rent By Owner Homes (RBOs) and other short-term private accommodations,
        have top-notch amenities with the best value, providing you with comfort and luxury at the same time. Get more value and more room when you stay at an RBO property in  <span>{{.LocationName}}</span>.</p>
{{ end }}
<p>
    Looking for last-minute deals, or finding the best deals available for cottages, condos, private villas, and large vacation
    homes? With RentByOwner <span>{{.LocationName}}</span>, you have the flexibility of comparing different options of various
    deals with a single click. Looking for an RBO with the best swimming pools, hot tubs, allows pets, or even those with
    huge master suite bedrooms and have large screen televisions? You can find vacation rentals by owner (RBOs), and other
    popular Airbnb-style properties in <span>{{.LocationName}}</span>. Places to stay near <span>{{.LocationName}}</span>
    {{ if gt .AverageRoomSize 0.0 }}
        are<span> {{.AverageRoomSize}} ft²</span> on average,
    {{ end }}
    {{ if gt .AveragePrice 0.0 }}
        with prices averaging <span id="js-average-price">{{.UserCurrency.Symbol}}{{UserPrice .AveragePrice .UserCurrency.Rate}}</span> a night.
    {{ end }}
</p>
<p>RentByOwner makes it easy and safe to find and compare vacation rentals in <span>{{.LocationName}}</span> with prices often at a 30-40% discount versus the price of a hotel. Just search for your destination and secure your reservation today.</p>""",
"key_4":"""RentByOwner makes it easy to compare the best listings on RBO homes from online vacation rental OTAs, including Booking.com and more. Use the Advanced Filter feature at the top to easily flip between RBO homes, vacation rentals, bed and breakfasts, private Airbnb-style rentals availability, eco-friendly properties, property type, cancellation policies, prices, and several different options. All these make it easier to find the perfect accommodation for your next vacation in {{.LocationName}}.""",
"key_5":"""{{template "sites/rentbyowner.com/layouts/main.tpl" .}}
{{template "common/details/published_details.tpl" .}}

{{define  "site_css_vars"}}
    <style>
        :root {
            /* Site 'Details' css image variable start*/
            --site-common-details-bottom-links-bullet: url({{.staticFileUrl}}/static/images/sites/rentbyowner.com/check.svg);
        }
    </style>
{{end}}

{{define "site_css"}}
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"/>
    <link rel="stylesheet" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"/>
    <link rel="stylesheet" type="text/css"
          href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"/>
{{end}}

{{define "site_preload"}}
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/variables.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/global.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/calendar.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/common/tiles.css"
          as="style"/>
    <link rel="preload" type="text/css" href="{{.staticFileUrl}}/static/css/sites/rentbyowner.com/pages/details.css"
          as="style"/>
{{end}}

{{define "site_details_popup_header"}}
    <img class="max-w-full nav-row-logo" loading="lazy"
         src="{{.staticFileUrl}}/static/images/sites/rentbyowner.com/header_logo.svg" alt="{{i18n .Lang "brand"}}"
         width="182"
         height="26">
{{end}}

{{define "details_breadcrumb"}}
    {{template "common/details/partials/details_breadcrumb.tpl" .}}
{{end}}

{{define "map_area_description"}}
    {{template "common/details/partials/details_area_description_map.tpl" .}}
{{end}}

{{define "seo_room_arragment_faq"}}
    {{template "common/details/partials/details_seo_room_arragment_faq.tpl" .}}
{{end}}

{{define "map"}}
    {{template "common/details/partials/details_map.tpl" .}}
{{end}}

{{define "details_faq"}}
    {{template "common/details/partials/faq.tpl" .}}
{{end}}

{{define "details_mobile_review"}}
    {{template "common/details/partials/details_mobile_reviews.tpl" .}}
{{end}}

<!-- Bedroom footer content start -->
{{define "site_bedroom_footer_content"}}
    <div class="bedroom-footer-content">
        <div class="bedroom-footer text-white" id="js-seo-block">
            <div class="max-container">
                <div class="container-fluid">
                    <h3 class="bedroom-footer-title font-20 no-margin pb-16 underlined-title">
                        Why is Rent By Owner {{.LocationName}} Your Choice for Vacation Rentals
                    </h3>
                    <div class="color-accent">
                        <p>Find your dream vacation rental on Rent By Owner, where
                            adventure meets comfort in every corner. RentByOwner features a broad mix of accommodations,
                            from charming country cottages and chic city apartments to tranquil beachfront villas and
                            cozy mountain cabins. Whether you're yearning for a delightful bungalow by the bay, a grand
                            estate over the dock, or a snug lodge in a quaint village, we've got the perfect spot for
                            you.</p>
                        <div class="{{if eq .UserInfo.Platform "mobile"}}hidden{{else}}visible{{end}}" id="js-seo-text-section">
                            <p>Prepare to unleash your inner explorer with our unique lodgings, including floating
                                houses, whimsical treehouses, and picturesque farmhouses, or stick to the classics with
                                duplexes, flats, and guesthouses. Choose the simplicity of a studio or the luxury of a
                                suite. For outdoor enthusiasts, we offer tents in hidden campsites, RVs, mountain
                                cabins, boat rentals, chalets in snowy havens, and caravans in lush gardens. Rent By
                                Owner truly has something for everyone.</p>
                            <p>Every holiday rental, from a humble hut to a lavish resort, guarantees a memorable stay
                                with cozy beds, functional kitchens, and welcoming living areas. Ideal for families,
                                couples, or solo adventurers, our rentals are more than just a place to sleep—they're
                                your home away from home. Book your next vacation with us and embark on a unique retreat
                                crafted for relaxation and adventure. We also offer annexes for added privacy, designer
                                lofts for a modern touch, and motels for quick stays. Explore beachside bungalows,
                                countryside ranches, and urban condos. Find your perfect getaway, whether it’s a quiet
                                den in the forest or a bustling inn by the island. At RentByOwner, our properties
                                include everything from houseboats and barns to court-style quarters and garden
                                retreats.</p>
                            <p>To make your booking experience even more convenient, we help you compare prices and
                                inventory so you can find and book your vacation rental on popular platforms like
                                Airbnb, Expedia, Vrbo (previously HomeAway), TripAdvisor (FlipKey), Booking.com, and
                                HomeToGo. We work with these trusted sites to offer you a seamless booking process,
                                ensuring that your perfect vacation rental is just a few clicks away.</p>
                        </div>
                    </div>
                    <div class="read-more-less {{if eq .UserInfo.Platform "mobile"}}visible{{else}}hidden{{end}}">
                        <div class="read-more cursor-pointer" id="js-seo-read-more">
                            <span class="text-white">{{i18n .Lang "__show_more"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                        <div class="read-less read-more-container cursor-pointer hidden" id="js-seo-read-less">
                            <span class="text-white">{{i18n .Lang "show_less"}}</span>
                            <svg class="icon text-white">
                                <use xlink:href="#chevron-down-solid"></use>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
{{end}}
<!-- Bedroom footer content start -->
"""
    }
    return tpls
